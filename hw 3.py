# Name:
# Student ID:
# Email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?

import random




class CouponDispenser:
   

    def __init__(self, coupon_cards):
    
        self.coupon_cards = coupon_cards
        self.customer_roster = []
        self.issued_indices = []


    def __str__(self):

        if not self.coupon_cards:
            return ""
        return "|".join(self.coupon_cards)

    def issue_coupon(self,name):
        
         if not self.coupon_cards:
             return "The box is empty."

         if name in self.customer_roster:
             index = self.issued_indices[self.customer_roster.index(name)]
             return f"That name already has a coupon: {self.coupon_cards[index]}"

         coupon_index = random.randint(0,len(self.coupon_cards) -1)
         self.customer_roster.append(name)
         self.issued_indices.append(coupon_index)
         return self.coupon_cards[coupon_index]

    def distribute_session(self):
         round_number = 1
         while True:
             user_input = input(
                 f"Round {round_number} - Enter a name (or a comma-separated list), or type 'show' or 'exit': "
             ).strip()

             if user_input == "exit":
                 print("Goodbye!")
                 break
    
             elif user_input == "show":
                 for i in range(len(self.customer_roster)):
                     print(f"{self.customer_roster[i]}: {self.coupon_cards[self.issued_indices[i]]}")
    
             else: 
                 names = user_input.split(",")
                 for n in names:
                     clean_name = n.strip()
                     if clean_name:
                         print(self.issue_coupon(clean_name))

             round_number += 1

    def tally_distribution(self):

         if not self.issued_indices:
            print("Empty")
            return

         for i, coupon in enumerate(self.coupon_cards):
             count = self.issued_indices.count(i)
             print(f"{coupon} distribution count: {count}.")

def main():

    coupon_cards = [
        "10% off",
        "Free small coffee",
        "Buy 1 get 1 half off",
        "Free extra espresso shot",
    ]

    box = CouponDispenser(coupon_cards)
    box.distribute_session()
    box.tally_distribution()

if __name__ == "__main__":
    main()
