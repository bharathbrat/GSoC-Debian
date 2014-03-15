from sqlalchemy import *
from matplotlib import pyplot as plt


engine = create_engine('postgresql://public-udd-mirror:\
public-udd-mirror@public-udd-mirror.xvm.mit.edu:5432/udd')
conn = engine.connect()

#read all the values from history.sources_count
result = conn.execute("select * from history.sources_count")
ts = []
arch = []
bzr = []
cvs = []
darcs = []
git = []
hg = []
mtn = []
svn = []
# Initialise lists to store values

for row in result:       #store the values
    ts.append(row['ts'])
    arch.append(row['vcstype_arch'])
    bzr.append(row['vcstype_bzr'])
    cvs.append(row['vcstype_cvs'])
    darcs.append(row['vcstype_darcs'])
    git.append(row['vcstype_git'])
    hg.append(row['vcstype_hg'])
    mtn.append(row['vcstype_mtn'])
    svn.append(row['vcstype_svn'])

#sort the lists according to the time
arch = [Y for (X,Y) in sorted(zip(ts, arch))]
bzr = [Y for (X,Y) in sorted(zip(ts, bzr))]
cvs = [Y for (X,Y) in sorted(zip(ts, cvs))]
darcs = [Y for (X,Y) in sorted(zip(ts, darcs))]
git = [Y for (X,Y) in sorted(zip(ts, git))]
hg = [Y for (X,Y) in sorted(zip(ts, hg))]
mtn = [Y for (X,Y) in sorted(zip(ts, mtn))]
svn = [Y for (X,Y) in sorted(zip(ts, svn))]
ts.sort()

#plot all the values on a single graph
p1, = plt.plot(ts, arch)
p2, = plt.plot(ts, bzr)
p3, = plt.plot(ts, cvs)
p4, = plt.plot(ts, darcs)
p5, = plt.plot(ts, git)
p6, = plt.plot(ts, hg)
p7, = plt.plot(ts, mtn)
p8, = plt.plot(ts, svn)
plt.xlabel('Date')
plt.ylabel('Number of packages')
plt.legend([p1,p2,p3,p4,p5,p6,p7,p8],['Arch','Bazaar','CVS','Darcs',\
                                      'Git','Mercurial','Monotone','Subversion'],9)
plt.show()
