# Class WIGDataRead : HDFから画像の情報や画像を呼び出すモジュール
import numpy as np
import pandas as pd
import h5py
from numpy.random import uniform, randint
from PIL import Image
from tensorflow.keras.utils import to_categorical
from sklearn import preprocessing

class WIGDataRead(object):
    '''     
    hdfdata, highest categolical index, index to be used for grouping, list of column index to be shown
    全データから取り出す最上位の項目（’’は全データ）、グループ化のカテゴリー（例えば属の場合'genus')、ピボットに表示する項目のリスト（通常帆はグループ化する項目の上位項目を選択
    example 
    pivot(f,'Fagaceae','species',['class', 'genus','species']) ブナ科のデータを取り出し、種レベルでグループ化して画像の総数を出力。
    pivot(f,'','genus',['class', 'genus']) 全ての科のデータを取り出し、属レベルでグループ化して画像の総数を出力。
    pivot(f,'','genus',['class', 'genus']) 全ての科のデータを取り出し、属レベルでグループ化して画像の総数を出力。

    '''
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.all_objs = []
        self.all_groups =[]
        self.all_datasets =[]
        self.data_num = []
        self.full_img_dir = []
        self.full_img_num = []
        self.train_imgs = []
        self.train_labels = []
        self.cat_train_labels=[]
        
    def list_contents(self, f):
        all_objs = []
        f.visit(all_objs.append)
        all_groups = [ obj for obj in all_objs if isinstance(f[obj],h5py.Group) ]
        all_datasets = [ obj for obj in all_objs if isinstance(f[obj],h5py.Dataset) ]
        return all_groups, all_datasets
    
    def list_class(self, f):
        return f.keys()

    def list_sel_genus(self,f,class_name):
        (af,ad) = self.list_contents(f)
        selected_groups = [ grp for grp in af if grp.startswith(class_name) ]
        selected_datasets = [ grp for grp in ad if grp.startswith(class_name) ]
        return selected_groups,selected_datasets
    
    def table_sel_genus(self,f,class_name):
        (af,ad)=self.list_sel_genus(f,class_name)
        data_num=[]
        for i in ad:
            data_num.append(f[i].shape[0])
        df=pd.DataFrame(ad,columns=['sample name'])
        df['img num']=data_num
        df = pd.concat([df['sample name'].str.split('/', expand=True),df], axis=1).drop('sample name', axis=1)
        df.rename(columns={0: 'class', 1: 'genus', 2: 'species', 3: 'source'}, inplace=True)
        return df
    
    def pivot(self,f,class_name,indexs={'class', 'genus','species'}): 
        df=self.table_sel_genus(f,class_name)
        pivtab = pd.pivot_table(df, values=['img num'], index=indexs, aggfunc=np.sum)
        return pivtab
    
    def list_sel_image_names(self, f, class_name):
        (af,ad)=self.list_sel_genus(f,class_name)
        full_img_dir=[]
        full_img_num=[]
        for k in range(len(ad)):  # list-up number of images in an individual sample
            for i in range(len(f[ad[k]])):
                full_img_dir.append(ad[k])
                full_img_num.append(i)
        all_index =(full_img_dir,full_img_num) # combine directory name and number of image
        all_img_index= np.array(all_index).T
        return all_img_index 
        

    def ImageDataGenerator(self, f, class_name='', target_label='species', size=(64,64), batch_size=100, shuffle=True):
        all_img_index=self.list_sel_image_names(f, class_name)
        train_imgs=[]
        cat_train_labels=[]
        rng = np.random.default_rng()
        while True:
            if shuffle:
                sh = np.random.permutation(np.arange(len(all_img_index)))
                path_sh = np.array(all_img_index)[sh] 
                label_sh = np.array(all_img_index)[sh]
            else:
                path_sh = all_img_index
                label_sh = all_img_index
                
                
            le = preprocessing.LabelEncoder()
            df_label=pd.DataFrame(label_sh.T[0],columns=['sample name'])
            df_label = pd.concat([df_label['sample name'].str.split('/', expand=True),df_label], axis=1).drop('sample name', axis=1)
            df_label.rename(columns={0: 'class', 1: 'genus', 2: 'species', 3: 'source'}, inplace=True)
            label_text=df_label[target_label]
            label_sh=le.fit_transform(df_label[target_label])
            label_num=len(np.unique(label_sh))
            
            for j,k,la,lat in zip(path_sh.T[0],path_sh.T[1],label_sh,label_text):     # zipは複数の変数をそれぞれ取得する際につかう
                gr=f[j][int(k)]
                f_rgb=np.dstack((gr,gr,gr))
                self.train_imgs.append(np.array(Image.fromarray(f_rgb).resize(size)))
                self.cat_train_labels.append(to_categorical(la,label_num))
                # batch_sizeの数だけ格納されたら、戻り値として返し、配列(self.iamges, self.labels)を空にする
                if len(self.train_imgs) == batch_size:
                    t_images = np.asarray(self.train_imgs,dtype=np.float32)
                    t_images /= 255.0
                    t_labels=np.asarray(self.cat_train_labels, dtype=np.float32)
                    self.reset()
                    yield t_images,t_labels


    def get_labels(self, f, class_name='', target_label='species'):
        all_img_index=self.list_sel_image_names(f, class_name)
        train_labels=[]
        label_se = all_img_index
                                
        le = preprocessing.LabelEncoder()
        df_label=pd.DataFrame(label_se.T[0],columns=['sample name'])
        df_label = pd.concat([df_label['sample name'].str.split('/', expand=True),df_label], axis=1).drop('sample name', axis=1)
        df_label.rename(columns={0: 'class', 1: 'genus', 2: 'species', 3: 'source'}, inplace=True)
        label_text=df_label[target_label]
            
        for lat in label_text:     # zipは複数の変数をそれぞれ取得する際につかう
            self.train_labels.append(lat)
        text_labels=np.asarray(self.train_labels)
        return text_labels

