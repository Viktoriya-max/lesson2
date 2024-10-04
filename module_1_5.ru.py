#1st exercise
immutable_var = 7,'раз отмерь',1.0,'отреж',True
print(immutable_var)
#2st exercise
immutable_var[0] = 1 #кортеж не поддерживает замену элементов
print(immutable_var)
#3st exercise
mutable_list=[1.0,"раз отмерь",7,"отреж",True]
print(type(mutable_list[0]))
mutable_list[0]=int(7)
print(type(mutable_list[0]))
mutable_list[2]=int(1.0)
print(mutable_list)
print(type(mutable_list[2]))
