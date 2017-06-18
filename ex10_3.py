def fn(l1):
 x= len(l1)
 new = []
 for i in range(x-1):
  new[i] = i+1 + l1[i]
 print new
fn([10,20,30,40])
