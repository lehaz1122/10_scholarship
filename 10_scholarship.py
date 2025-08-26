std_fee = 1000


std_class = "matric"

if std_class == "matric":
    std_marks = int(input("Enter your Marks: "))
    if std_marks >= 1200:
      print("congratulations! You got 100% Scholarship")
    elif std_marks >= 1100:
     print(f"Congratulations! you got 90% scholarship. total fee is {std_fee} but after getting scholarship your fee is", std_fee - 100 * 0.9)
    else:
      print("We are sorry you're not eligigle for scholarship")
else:
  print("We have no scholarship for other grades")