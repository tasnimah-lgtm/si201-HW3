# Name: Tasnimah uddin
# Student ID: 3176 9013
# Email: tasnimah@umich.edu
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
    

