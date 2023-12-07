import math_operations
import temperature_conversion
import validation
import geometry

res1 = math_operations.plus(7,5)
res2 = math_operations.minus(7,5)
res3 = math_operations.mult(7,5)
res4 = math_operations.div(7,5)
print(res1,res2,res3,res4)

res = temperature_conversion.ctof(24)
res2 = temperature_conversion.ftoc(75.2)
print(res, res2)

valid = validation.val(2)
valid2 = validation.val(3)
print(valid, valid2)

Scircle = geometry.circle(4)
Striangle = geometry.triangle(10,5)
Srectangle = geometry.rectangle(4,4)
print(Scircle,Striangle,Srectangle)
