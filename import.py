import bpy

n = 50000
prime = []
for i in range(n+1):
    prime.append(True)
 
p = 2
while (p * p <= n):  
    if prime[p]: 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1

x = 2
y = 3
for i in range(5,n):
    if prime[i] == True:
        bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, location=(x, y, i))
        x = y
        y = i