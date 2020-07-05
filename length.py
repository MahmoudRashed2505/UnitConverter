class unit:
    unitName = None
    unitCode = None
    def __init__(self,name,code):
        self.unitName = name
        self.unitCode = code
        self.conversionRate = dict()
    def addRate(self,unit,rate):
        self.conversionRate[unit]=rate

units =[]

km = unit('Kilometer','km')
km.addRate('m',"1000")
km.addRate('cm',"100000")
km.addRate('mm',"1,000,000,000")
km.addRate('mi',"0.621371")
km.addRate('yd',"1093.61")
km.addRate('ft',"3280.84")
km.addRate('in',"39370.1")

units.append(km)

m = unit("Meter",'m')
m.addRate("km","0.001")
m.addRate("cm","100")
m.addRate("mm","1000")
m.addRate("mi","0.000621371")
m.addRate("yd","1.09361")
m.addRate("ft","3.28084")
m.addRate("in","39.3701")

units.append(m)

cm = unit("Centimeter",'cm')
cm.addRate("km","0.00001")
cm.addRate("m","0.01")
cm.addRate("mm","10")
cm.addRate("mi","0.000006")
cm.addRate("yd","0.0109361")
cm.addRate("ft","0.0328084")
cm.addRate("in","0.393701")

units.append(cm)

mm = unit("Millimeter",'mm')
mm.addRate("km","0.000001")
mm.addRate("m","0.001")
mm.addRate("cm","0.1")
mm.addRate("mi","0.000000621371192")
mm.addRate("yd","0.001094")
mm.addRate("ft","0.003281")
mm.addRate("in","0.03937")

units.append(mm)

inch = unit("Inch",'in')
inch.addRate("km","0.000025")
inch.addRate("m","0.0254")
inch.addRate("cm","2.54")
inch.addRate("mi","0.000016")
inch.addRate("yd","0.027778")
inch.addRate("ft","0.083333")
inch.addRate("mm","25.4")

units.append(inch)

yd = unit("Yards",'yd')
yd.addRate("km","0.000914")
yd.addRate("m","0.9144")
yd.addRate("cm","91.44")
yd.addRate("mi","0.000568")
yd.addRate("mm","914.4")
yd.addRate("ft","3")
yd.addRate("in","36")

units.append(yd)

mi = unit("Miles",'mi')
mi.addRate("km","1.609344")
mi.addRate("m","1609.344")
mi.addRate("cm","160,934.4")
mi.addRate("mm","1609344")
mi.addRate("yd","1,760")
mi.addRate("ft","5,280")
mi.addRate("in","63,360")

units.append(mi)

ft = unit("Feat",'ft')
ft.addRate("km","0.000305")
ft.addRate("m","0.3048")
ft.addRate("cm","30.48")
ft.addRate("mi","0.000189")
ft.addRate("yd","0.333333")
ft.addRate("mm","304.8")
ft.addRate("in","12")

units.append(ft)

amount = float(input("Please Enter the amount: "))
print()

unitNumber = 0
for count in units:
    print("{} -) {} ---> {}".format(unitNumber+1,units[unitNumber].unitName,units[unitNumber].unitCode))
    unitNumber += 1

baseUnit = int(input("\nPlease Choose The Number of Base Unit: "))
baseUnit = units[baseUnit-1]
convertedUnit = int(input("Please Choose the number of the desired unit: "))
convertedUnit = units[convertedUnit-1]


convertedamount = float(baseUnit.conversionRate.get(convertedUnit.unitCode)) * amount

print("\n{} {} = {:.4f} {}".format(amount,baseUnit.unitCode,convertedamount, convertedUnit.unitCode))

