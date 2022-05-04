def leap_gen(yr1,yr2):
    for i in range(yr1,yr2+1):
        yield i
def leap_year(yr1,yr2):
    leap_year=[]
    gener = (i for i in range(yr1,yr2+1))
    for i in range(yr1,yr2+1):
                yr=next(gener)
                if yr%4==0 and yr%100 !=0:
                    leap_year.append(yr)
                elif yr%400==0 and yr%100==0:
                    leap_year.append(yr)
                else:
                    continue
    return leap_year
