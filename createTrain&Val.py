import os
import shutil
import scipy

# Pega todo caminho
base_dir = os.getcwd()
# Pega o caminho e atribui as variaveis
CincoCentDir = os.path.join(base_dir,'dataset/0/')
DezCentDir = os.path.join(base_dir,'dataset/1/')
VinteCincoCentDir = os.path.join(base_dir,'dataset/2/')
CinquentaCentDir = os.path.join(base_dir,'dataset/3/')
UmRealCentDir = os.path.join(base_dir,'dataset/4/')

# verificar se esta carreando todas as imagens
cincoCent_images = os.listdir(CincoCentDir)
dezCent_images = os.listdir(DezCentDir)
vinteCincoCent_images = os.listdir(VinteCincoCentDir)
cinquentaCent_images = os.listdir(CinquentaCentDir)
umRealCent_images = os.listdir(UmRealCentDir)

print('quantidade de imagem em cada cada pasta respectivamente:',len(cincoCent_images), len(dezCent_images), len(vinteCincoCent_images), len(cinquentaCent_images), len(umRealCent_images))


train_cincoCent_images = cincoCent_images[:int(.8*(len(cincoCent_images)))]
val_cincoCent_images = cincoCent_images[int(.8*(len(cincoCent_images))):]

train_dezCent_images = dezCent_images[:int(.8*(len(dezCent_images)))]
val_dezCent_images = dezCent_images[int(.8*(len(dezCent_images))):]

train_vinteCincoCent_images = vinteCincoCent_images[:int(.8*(len(vinteCincoCent_images)))]
val_vinteCincoCent_images = vinteCincoCent_images[int(.8*(len(vinteCincoCent_images))):]

train_cinquentaCent_images = cinquentaCent_images[:int(.8*(len(cinquentaCent_images)))]
val_cinquentaCent_images = cinquentaCent_images[int(.8*(len(cinquentaCent_images))):]

train_umRealCent_images = umRealCent_images[:int(.8*(len(umRealCent_images)))]
val_umRealCent_images = umRealCent_images[int(.8*(len(umRealCent_images))):]

# Criando arquivos nas pastas de treino e test
train_dir = 'train_data/'
val_dir = 'val_data/'

try:
    os.makedirs(os.path.join(base_dir, train_dir, '5/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, train_dir, '10/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, train_dir, '25/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, train_dir, '50/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, train_dir, '100/'))
except:
    pass

try:
    os.makedirs(os.path.join(base_dir, val_dir, '5/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, val_dir, '10/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, val_dir, '25/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, val_dir, '50/'))
except:
    pass
try:
    os.makedirs(os.path.join(base_dir, val_dir, '100/'))
except:
    pass

for image in train_cincoCent_images:
    src = CincoCentDir + image
    dst = os.path.join(base_dir, train_dir, '5/')
    shutil.copy(src, dst)

for image in train_dezCent_images:
    src = DezCentDir + image
    dst = os.path.join(base_dir, train_dir, '10/')
    shutil.copy(src, dst)

for image in train_vinteCincoCent_images:
    src = VinteCincoCentDir + image
    dst = os.path.join(base_dir, train_dir, '25/')
    shutil.copy(src, dst)

for image in train_cinquentaCent_images:
    src = CinquentaCentDir + image
    dst = os.path.join(base_dir, train_dir, '50/')
    shutil.copy(src, dst)

for image in train_umRealCent_images:
    src = UmRealCentDir + image
    dst = os.path.join(base_dir, train_dir, '100/')
    shutil.copy(src, dst)

for image in val_cincoCent_images:
    src = CincoCentDir + image
    dst = os.path.join(base_dir, val_dir, '5/')
    shutil.copy(src, dst)

for image in val_dezCent_images:
    src = DezCentDir + image
    dst = os.path.join(base_dir, val_dir, '10/')
    shutil.copy(src, dst)

for image in val_vinteCincoCent_images:
    src = VinteCincoCentDir + image
    dst = os.path.join(base_dir, val_dir, '25/')
    shutil.copy(src, dst)

for image in val_cinquentaCent_images:
    src = CinquentaCentDir + image
    dst = os.path.join(base_dir, val_dir, '50/')
    shutil.copy(src, dst)

for image in val_umRealCent_images:
    src = UmRealCentDir + image
    dst = os.path.join(base_dir, val_dir, '100/')
    shutil.copy(src, dst)



