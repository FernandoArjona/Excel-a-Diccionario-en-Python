#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import *    


# In[2]:


print('FERNANDO ARJONA LIRA --- 2943290')
print('EVIDENCIA AVANCE 1 --- DICCIONARIO')
print('Se van a cargar y procesar archivos, favor de tener paciencia...')


# In[3]:


paths = []
#REMPLAZAR ESTOS DIRECTORIOS CON AQUELLOS QUE QUIERA ANALZIAR DESDE SU MÁQUINA
paths.append('C:/Users/Fernando/Documents/Escritorio/excel files/aisles.csv')
paths.append('C:/Users/Fernando/Documents/Escritorio/excel files/departments.csv')
paths.append('C:/Users/Fernando/Documents/Escritorio/excel files/products.csv')


# In[4]:


dictionaries = []


# In[5]:


for k in range(len(paths)):
    excel = read_csv(paths[k])
    keys = list(excel.iloc[:, 0])
    values = []
    for i in range(len(excel)):
        new_value = list(excel.iloc[i, :])
        new_value.pop(0)
        values.append(new_value)
        
    dictionary = {}
    for key in keys:
        for value in values:
           dictionary[key] = value
           values.remove(value)
           break
       
    dictionaries.append(dictionary)
    print('Archivo ' + str(k) + ' de 7 procesado')


# In[6]:


print('DICCIONARIO 0:')
print(dictionaries[0])

print('DICCIONARIO 1:')
print(dictionaries[1])

print('DICCIONARIO 2:')
print(dictionaries[2])


# In[ ]:




