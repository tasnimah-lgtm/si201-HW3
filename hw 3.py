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
