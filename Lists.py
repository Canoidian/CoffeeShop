#supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
#camp_site = ["Crystal Lake", 404, 95.5, 10, False]
#bernard = supplies[0]
#print(bernard)

#Python List
camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]
#print(type(camping_list))

camp_site = ["Crystal Lake", 404, 37.9, True]

Chuck = camping_list[4]
# [-1] is a negative index, used to access the last thing in your list. [-2] is the second last thing in the list
William = camping_list[-1]

#print(Chuck)
#print(William)



# How to add to lists one at a time. Though this only adds it to the end of the list
#camping_list.append("toilet paper")

# Adds multiple things to a list. Though this only adds it to the end of the list
camping_list.extend(["toilet paper", "tea"])
# Another way to add multiple things to a list
#camping_list = camping_list + ["toilet paper", "tea"]

#print(camping_list)

# How to add something to a specific place in a list. 0 is the index/ the place you want your thing to be in the list
camping_list.insert(0, "chocolate")


# How to remove everything from a list
#camping_list.clear()

# How to remove one thing from a list
#camping_list.remove("tent")

# Remove with index
camping_list.pop(1)

print("TThe item " + camping_list.pop(1) + " was just deleted")