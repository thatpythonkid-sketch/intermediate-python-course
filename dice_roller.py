import random

def main():
  dice_rolls = 6
  dice_sum = 0
  dice_size = 6
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    yahtzee_total = 0
    num1_total = 0
    num2_total = 0
    num3_total = 0
    num4_total = 0
    num5_total = 0
    num6_total = 0
    if roll == 1:
      print(f"you rolled a {roll}!")
      num1_total += 1
    elif roll == dice_size:
      print(f"you rolled a {roll}!")
      num6_total += 1
    elif roll == 2:
      print(f"you rolled a {roll}!")
      num2_total += 1
    elif roll == 3:
      print(f"you rolled a {roll}!")
      num3_total += 1
    elif roll == 4:
      print(f"you rolled a {roll}!")
      num4_total += 1
    elif roll == 5:
      print(f"you rolled a {roll}!")
      num5_total += 1
    elif roll == roll == roll == roll == roll:
      print("yahtzee!")
      yahtzee_total += 1
  print(f"you rolled {yahtzee_total} yahtzee's! ")
  print(f"you rolled {num1_total} number 1's")
  print(f"you have rolled a total of {dice_sum}")


if __name__== "__main__":
    main()