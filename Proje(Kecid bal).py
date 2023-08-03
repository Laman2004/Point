with open("Mixdata.txt") as f:
    with open("Newdata1.txt","w") as g:
        with open("Newdata2.txt","w") as k:
            inner=f.readlines()
            m=0
            for row in inner:
                if m==0:
                    m+=1
                    continue
                row=row.replace("\n","")
                space_num=0
                space_indexs=[]
                index=0
                for value in row:
                    if value==" ":
                        space_num+=space_num
                        space_indexs.append(index)
                    index+=1
                ad_soyad=row[:space_indexs[0]]
                soyad=ad_soyad.split("-")[-1]
                ad=ad_soyad[:ad_soyad.index(soyad)-1].replace("-"," ")
                points=row.split(" ")[-1]
                points=points.split("/")
                point1= int(points[0])
                point2= int(points[1])
                final= int(points[2])
                ortalama=point1*0.3+point2*0.3+final*0.4
                specialty=row[space_indexs[0]+1:space_indexs[len(space_indexs)-1]]
                if ortalama>=70 and final>=70:
                    g.write(ad)
                    g.write(" "*(25-len(ad)))
                    g.write(soyad)
                    g.write(" "*(25-len(soyad)))
                    g.write(specialty)
                    g.write(" "*(25-len(specialty)))
                    g.write(str(round(ortalama,1)))
                    g.write(" "*21)
                    g.write("Passed")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(specialty)
                    k.write(" " * (25 - len(specialty)))
                    k.write(str(round(ortalama, 1)))
                    k.write(" " * 21)
                    k.write("Failed")
                    k.write("\n")