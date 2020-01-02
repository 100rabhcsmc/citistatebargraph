import matplotlib.pyplot as plt

states=["Maharashtra", 'Delhi', 'Karnataka', 'Gujarat', 'Telangana', 'Tamil Nadu', 
'West Bengal', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 'Madhya Pradesh', 
'Andhra Pradesh', 'Punjab', 'Haryana', 'Jammu and Kashmir', 'Jharkhand', 
'Chhattisgarh', 'Assam', 'Chandigarh', 'Odisha', 'Kerala', 'Uttarakhand',
 'Puducherry', 'Tripura', 'Mizoram', 'Meghalaya', 'Manipur', 'Himachal Pradesh', 
 'Nagaland', "Goa", "Andaman and Nicobar Islands", "Arunachal Pradesh", 
 "Dadra and Nagar Haveli", "Himachal Praddesh"
 ]

cities=[ 120,  2,  80,  73,  40,  112,
 44, 78, 118,  70, 82,
  83, 54, 37, 9,  27,
   19,  26,  1, 34, 51, 18,
    4,  7,  3,  3, 4,  7,
    6, 4,1, 2, 
    1,1
  ]

plt.title(" cities and states")
plt.xlabel("no of states")
plt.ylabel("no of cities")

plt.bar(states,cities )
plt.xticks(rotation=90)
plt.show()

