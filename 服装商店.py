print("===================================")
print("              服装商店               ")
print("===================================")
print("日期 服装名称 价格/件 库存数量 销售量/每日")
print("1号  羽绒服   253.6   500      10")
print("2号  牛仔裤    86.3   600      60")
print("3号   风衣     96.8   355      43")
print("4号   皮草     135.9  855      63")
print("5号   T恤      65.8   632      63")
print("6号   衬衫     49.3   562      120")
print("7号  牛仔裤    86.3    600      90")
print("8号  羽绒服    253.6   500      69")
print("9号  牛仔裤    86.3    600      35")
print("10号 羽绒服    253.6   500     140")
print("11号 牛仔裤    86.3    600      90")
print("12号  皮草    135.9    855      24")
print("13号  T恤     65.8     632      45")
print("14号  风衣    96.8     355      25")
print("15号  牛仔裤  86.3     600      129")
print("16号  T恤    65.8     632      129")
print("17号  羽绒服  253.6    500       10")
print("18号  风衣    96.8     335      43")
print("19号  T恤     65.8     632      63")
print("20号  牛仔裤   86.3     600      60")
print("21号  皮草     135.9    855      63")
print("22号	 风衣	 96.8	  335	   60")
print("23号	 T血	 65.8	  632	   58")
print("24号	 牛仔裤	 86.3	  600	  140")
print("25号	 T血	 65.8	  632	  48")
print("26号	 风衣	 96.8	 335	  43")
print("27号	 皮草	 135.9	 855	  57")
print("28号	 羽绒服	 253.6	 500	 10")
print("29号	 T血	 65.8	 632	 63")
print("30号	 风衣	 96.8	 335	 78")
money1=(236.6*(10+69+140+10+10)+86.3*(60+90+35+90+129+60+140)+96.8*(43+25+43+60+43+78)+135.9*(63+24+63+57)+65.8*(63+45+129+63+58+48+63)+49.3*120)
print("总价格：",money1)
money2=((10+69+140+10+10+60+90+35+90+129+60+140+43+25+43+60+43+78+63+24+63+57+63+45+129+63+58+48+63+120)/30)
money2 = int(money2)
print("平均每日销售数量：",money2)
money3=(10+69+140+10+10+60+90+35+90+129+60+140+43+25+43+60+43+78+63+24+63+57+63+45+129+63+58+48+63+120)
money4=('{:.0%}'.format((10+69+140+10+10)/money3))
print("每个种类月销售量占比:")
print("羽绒服：",money4)
money5=('{:.0%}'.format((60+90+35+90+129+60+140)/money3))
print("牛仔裤：",money5)
money6=('{:.0%}'.format((43+25+43+60+43+78)/money3))
print("风衣：",money6)
money7=('{:.0%}'.format((63+24+63+57)/money3))
print("皮草：",money7)
money8=('{:.0%}'.format((63+45+129+63+58+48+63)/money3))
print("T恤：",money8)
money9=('{:.0%}'.format(120/money3))
print("衬衫",money9)