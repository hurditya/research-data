import pandas as pd

dataset = pd.read_csv(' .csv')                  #Enter dataset name here

dataset = pd.DataFrame(dataset)

data = dataset[dataset['Kind'].str.contains('Class') == True]

data = data[['Kind', 'Name', 'CountLine' ,'CountLineCode', 'CountLineBlank', 'CountLineComment', 
             'CountClassBase', 'CountClassCoupled', 'CountClassDerived', 'CountDeclClassMethod', 
             'CountDeclClassVariable', 'CountDeclInstanceMethod', 'CountDeclInstanceVariable', 
             'CountDeclMethod', 'CountDeclMethodAll', 'CountDeclMethodDefault',
             'CountDeclMethodPrivate', 'CountDeclMethodProtected', 'CountDeclMethodPublic', 
             'MaxInheritanceTree', 'PercentLackOfCohesion']]

data.to_csv(' .csv')                             #Enter destination file here
