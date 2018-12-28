###########################################################
# This util is to calculate RA-RNTI in NR5G
# Based on 38.321 and 38.211
# Currently limitation :
#                       Random access configurations for FR1 and unpaired spectrum
#                       only for NUL carrier
#                       Only for FR1 (30Khz)
###########################################################
import math
from sys import exit
# s_id
# t_id
# f_id

prach_cfg_idx_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255]
x = [16,8,4,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,1,16,8,4,2,2,1,16,8,4,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,16,1,1,2,1,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,4,2,2,2,2,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,16,8,4,2,2,2,2,2,2,2,8,4,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1]
y = [1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
prach_duration_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,2,2,2,2,2,2,2,2,2,2,2,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
starting_symbol_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,0,0,0,0,0,7,0,0,0,7,0,0,0,7,0,0,0,0,0,9,9,0,0,0,0,0,0,9,0,0,0,0,9,0,0,0,9,0,0,0,7,7,0,0,0,0,0,0,0,0,7,0,0,0,0,7,0,0,0,7,2,2,2,8,2,2,8,2,2,2,8,2,0,0,2,0,2,2,2,0,0,0,0,0,0,0,0,2,0,2,2,0,2,2,0,2,2,2,2,2,2,2,8,8,2,2,2,8,2,2,2,8,2,2,2,8,2,2,2,2,2,2,8,8,2,2,8,8,2,8,2,2,2,8,2,2,2,8,2,8,8,2,2,2,2,8,2,2,2,8,2,2,8,0,6,6,0,0,0,6,0,0,0,6,0,0,0,6,0,2,0,2,0,0,0,2,0,0,0,2,0,0,2]
sf_number =    [[9],[9],[9],[9],[9],[4],[4],[9],[8],[7],[6],[5],[4],[3],[2],[1,6],[1,6],[4,9],[3,8],[2,7],[8,9],[4,8,9],[3,4,9],[7,8,9],[3,4,8,9],[6,7,8,9],[1,4,6,9],[1,3,5,7,9],[7],[7],[7],[7],[7],[7],[6],[6],[6],[6],[6],[6],[9],[9],[9],[9],[9],[4],[4],[9],[8],[7],[6],[5],[4],[3],[2],[1,6],[1,6],[4,9],[3,8],[2,7],[8,9],[4,8,9],[3,4,9],[7,8,9],[3,4,8,9],[1,4,6,9],[1,3,5,7,9],[9],[9],[9],[9],[4,9],[7,9],[7,9],[8,9],[4,9],[2,3,4,7,8,9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[9],[9],[7,9],[8,9],[7,9],[4,9],[4,9],[2,3,4,7,8,9],[2],[7],[9],[9],[9],[9],[2,7],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[9],[9],[4,9],[7,9],[7,9],[4,9],[8,9],[2,3,4,7,8,9],[2],[7],[9],[9],[9],[9],[2,7],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[9],[7,9],[4,9],[4,9],[9],[9],[9],[8,9],[4,9],[7,9],[1,3,5,7,9],[9],[9],[9],[9],[9],[7,9],[4,9],[4,9],[8,9],[2,3,4,7,8,9],[1],[2],[4],[7],[9],[9],[9],[4,9],[7,9],[8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[9],[9],[9],[9],[8,9],[7,9],[7,9],[4,9],[4,9],[2,3,4,7,8,9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[9],[9],[9],[8,9],[7,9],[7,9],[4,9],[4,9],[2,3,4,7,8,9],[9],[9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[4,9],[7,9],[7,9],[4,9],[8,9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[4,9],[7,9],[4,9],[8,9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9],[9],[4,9],[7,9],[7,9],[4,9],[8,9],[9],[9],[9],[8,9],[4,9],[7,9],[3,4,8,9],[1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9]]
slot_num_sf = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
def tdd_slot(rat_type):
        tdd_periodicity = int(raw_input("INPUT: TDD periodicity in ms > "))
        # num_ul_slots = int(raw_input("INPUT: Number of UL Slots in TDD Pattern > "))
        tdd_periodicity_slot = (tdd_periodicity*2)-1
        valid_ra_slot = []
        for i in slot_num_sf:
            if i%tdd_periodicity_slot == 0:
                valid_slots = slot_num_sf.pop(i-1)
                valid_ra_slot.append(i)
        valid_ra_slot.remove(0)
        print "\nValid RA slot number(s)",valid_ra_slot
pass

def fdd_slot(rat_type):
    valid_ra_slot = []
    for i in valid_sf_num:
        valid_slots = (2*i)-1
        valid_ra_slot.append(valid_slots)
        print "\nValid RA slot number(s)",valid_ra_slot
    pass
config_idx = int(raw_input("INPUT: Prach Config Index > "))
prach_cfg_idx = prach_cfg_idx_list.index(config_idx)
prach_duration = prach_duration_list.pop(prach_cfg_idx)
starting_symbol = starting_symbol_list.pop(prach_cfg_idx)
x_idx = x.pop(prach_cfg_idx)
y_idx = y.pop(prach_cfg_idx)
prach_strt_symbol = starting_symbol_list.pop(prach_cfg_idx)

print "\nFor Prach Config Index %i\nPrach duration = %i symbols \nPRACH Starting symbol = %i" %(config_idx, prach_duration,starting_symbol)
valid_prach_sfn = []
for sfn in range(0,1024):
    if sfn%x_idx == y_idx:
        valid_prach_sfn.append(sfn)
print "\nBelow is a list of valid prach SFN\n",valid_prach_sfn
print "\nPrach starting symbol = ",prach_strt_symbol
valid_sf_num = sf_number.pop(prach_cfg_idx)
print "Valid Subframes in the every valid SFN = ", valid_sf_num
rat_type = raw_input("Is RAT Type TDD or FDD > ").upper()
# slot_num = int(raw_input("UL Slot number in the SF [0 or 1] > "))
if rat_type == "TDD":
    tdd_slot(rat_type)
else:
    fdd_slot(rat_type)