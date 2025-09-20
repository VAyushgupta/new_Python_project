# import re
#
# r = '''Physical volume 'dev/sda' created Successfully
# Physical volume 'dev/sdb' created Successfully
# Physical volume 'dev/sdc' created Successfully'''
# for n in r.split('\n'):
#     match = re.search(r"Physical volume 'dev/sd[a-z]' created Successfully",n)
#     if match:
#         return True
#     else:
#         raise Exception("Error in Creating volume")