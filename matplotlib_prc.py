import matplotlib.pyplot as plt
import numpy as np
m = ['jan','feb','mar']
pe = [100,90,95]
pc = [120,110,115]
pg = [80,70,85]
oe = [150,140,160]
oc = [180,160,190]
og = [130,120,140]
x = np.arange(len(m))
w = 0.2

fig,ax = plt.subplots(figsize=(8,6))
ax.bar(x-w/2,pe,w,label ="PE")
ax.bar(x-w/2,pc,w,bottom = pe,label='PC')
ax.bar(x-w/2,pg,w,bottom=np.array(pe)+np.array(pc),label="PG")
ax.bar(x+w/2,oe,w,label='OE')
ax.bar(x+w/2,oc,w,bottom = oe,label='OC')
ax.bar(x+w/2,og,w,bottom = np.array(oe)+np.array(oc),label="OG")

ax.set_xlabel("month")
ax.set_ylabel("sales")
ax.set_title("sale comp")
ax.set_xticks(x)
ax.set_xticklabels(m)
ax.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
plt.plot(m,pe,label='PE',marker='o')
plt.plot(m,pc,label='PC',marker='v')
plt.plot(m,pg,label="PG",marker='<')
plt.plot(m,oe,label='OE',marker='>')
plt.plot(m,oc,label='OC',marker='+')
plt.plot(m,og,label='OG',marker='o')

plt.xlabel('MONTH')
plt.ylabel('sales')
plt.title('sales trends')
plt.legend()
plt.tight_layout()
#plt.show()