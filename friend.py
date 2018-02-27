from SocialNetwork import Friend
f = { "A" : ["D"],
      "B" : ["C"],
      "C" : ["B", "D", "E"],
      "D" : ["A", "C"],
      "E" : ["C"],
      "F" : []
           }
friend = Friend(f)
print("Initial social network:")
print(friend)
print("Check if A,B can be connected:")
print(friend.can_be_connected("A", "B"))
print("Check if A,F can be connected:")
print(friend.can_be_connected("A", "F"))

print("After add people Z, the social network is:")
friend.add_people("Z")
print(friend)
print("Before add connection, check if F,Z can be connected:")
print(friend.can_be_connected("F", "Z"))
friend.add_connection(('F', 'Z'))
print("After add connection, check if F,Z can be connected:")
print(friend.can_be_connected("F", "Z"))
