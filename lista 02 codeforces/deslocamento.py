dist = int(input())
vm = int(input())
h = int(dist // vm)
m = int(((dist / vm) - h) * 60)
print("{:02d}".format(h),"{:02d}".format(m),sep=":")