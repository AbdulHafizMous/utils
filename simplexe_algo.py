# from scipy.optimize import linprog as ln

# # c= [-1, 4]
# # A = [[-3, 1],[1, 2]]
# # b = [6, 4]
# # x0_bounds = (0, None)
# # x1_bounds = (0, None)
# # res = ln(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
# # print(f'Z* = {res.fun} \nX* = {res.x} \n{res.message}')



# # Exo 1

# c= [-5, -1]
# A = [[-1, 2],[1, -1], [4, 1]]
# b = [4, 1, 12]
# x0_bounds = (0, None)
# x1_bounds = (0, None)
# res = ln(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], integrality=1)
# print(f'Z* = {-1*res.fun} \nX* = {res.x} \n{res.message}')



# # Exo 2

# '''

# Min 4,5x1 + 7,8x2 + 3,6x3 + 3,1x4 + 4,9y1 + 7,2y2 + 4,3y3 + 2,9y4
#        x1 +    x2 +    x3 +    x4                                 = 2
#                                        y1 +    y2 +    y3 +    y4 = 2
#        x1 +                            y1                         = 1
#                x2 +                            y2                 = 1
#                        x3 +                            y3         = 1
#                                x4 +                            y4 = 1

#        x1 ;    x2 ;    x3 ;    x4 ;    y1 ;    y2 ;    y3 ;    y4 £ {0, 1}



# '''


# from scipy.optimize import linprog
# c= [4.5, 7.8, 3.6, 3.1, 4.9, 7.2, 4.3, 2.9]
# A = [
#         [1, 0, 0, 0, 1, 0, 0, 0],
#         [0, 1, 0, 0, 0, 1, 0, 0],
#         [0, 0, 1, 0, 0, 0, 1, 0],
#         [0, 0, 0, 1, 0, 0, 0, 1],

#         [1, 1, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 1, 1],
#     ]
# b = [
#         1,
#         1,
#         1,
#         1,

#         2,
#         2
# ]
# x1_bounds = (0, None)
# x2_bounds = (0, None)
# x3_bounds = (0, None)
# x4_bounds = (0, None)
# y1_bounds = (0, None)
# y2_bounds = (0, None)
# y3_bounds = (0, None)
# y4_bounds = (0, None)

# res = ln(c, A_eq=A, b_eq=b, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds, y1_bounds, y2_bounds, y3_bounds, y4_bounds ], integrality=1)
# print(f'Z* = {res.fun} \nX* = {res.x} \n{res.message}')


from scipy.optimize import linprog
C =[2, 5, 3, 0, 0]
# C =[0, 0.5, 0, 0.5, 2]
A = [[0, 1.5, 1, -1.5, 0],[1, -2.5, 0, 0.5, -1]]
B = [1, 2]
a =(0,None)
b =(0,None)
c =(0,None)
d =(0,None)
e =(0,None)

res = linprog(C, A_eq=A, b_eq=B , bounds=[a,b,c,d,e])
#res *=-1
print(f"\nLe cout optimal est Z* = {-res.fun} \nLa solution optimale est X* = {res.x}")
print(res.message)