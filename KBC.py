questions = [
    [
    "Who is PM of india?","Modi","Gandhi","Kejriwal","Thackray",1
    ],

            [
                "What is the captial of india?","Mumbai","Pune","Delhi","Chennai",3
                ],

            [
                "National animal of india?","Peacock","Tiger","Lion","Croc",2
             ],

             [
                  "Which state is the largest producer of sugarcane in India?",
         "Maharashtra","Karnataka","Madhya Pradesh","Uttar Pradesh",4
             ],

             [
                 "Which part of the plant absorbs water and nutrients from the soil?",
             "Stem","Buds","Leafs","Root",4
             ],

             [
                 "For which of those groups has MS Dhoni performed two seasons in IPL?",
                "Chennai Super Kings","Rising Pune Supergiants","Deccan Chargers","Gujrat Lions",2
             ],

             [
                  "Which ingredient is mixed in milk is a popular home remedy for healing any internal injury?",
                    "Lemon","Honey","Almond","Turmeric",4
             ],

             [
                  "Which of the following companies was originally started as a loom manufacturing unit in 1909?",
      "Suzuki","CEAT","Honda","Mercedes",1
             ],

             [
                "Besides Sachin Tendulkar , who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
     "Virat Kohli","Sunil Gavaskar","VVS laxman","Rahul Dravid",4
             ],

             [
                 "Who was the Defense Minister of India when the India-China War of 1962 began?",
              "VK Krishna Menon","Rajnath Singh","Manohar Parrikar","Nirmala Sitharaman",1
             ],
            ]
money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
level = 0
for i in range(0,len(questions)):
    question = questions[i][0]
    answer = questions[i]
    print(f"\n\nQuestion for Rs. {money[i]}")
    print(f"\nQuestion : {question}")
    print(f"1.{answer[1]}       2.{answer[2]}")
    print(f"3.{answer[3]}       4.{answer[4]}")
    user = int(input("Enter your answer (1-4) or press 0 to quit : " ))
    if user == 0:
        level = money[i-1]
        break
    if user == answer[5]:
        print("Correct Answer")
        print(f"You won Rs.{money[i]}")
        
        if i == 3 :
            print(f"You have won Rs.{money[3]}")
        elif i == 6:
            print(f"You have won Rs. {money[6]}")
    
    else :
        print("Wrong answer")
        break 

print(f"The total amount you won is: Rs.{money[i-1]} ")

