anime_list=["naruto","luffy","ichigo","gojo","goku"]

anime_list.append("zoro")

anime_list.remove("gojo")

anime_list[4]="madara"


print("\nUpdated list :  ",anime_list)

anime_dict={'name':'naruto','age':21,'city':'konoha'}

anime_dict['gender']='male'

del anime_dict['city']

anime_dict['age']=31

print("\nUpdated dictonary :  ",anime_dict)


anime_set={"naruto","luffy","ichigo","gojo"}

anime_set.add("zoro")

anime_set.remove("gojo")

anime_set.discard("naruto")
anime_set.add("itachi")

print("\nUpdated set :  ",anime_set)