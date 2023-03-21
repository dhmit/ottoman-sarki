NAME_TO_MSTRKS = [
  ({"Rast", "Evc", "Rehavi", "Pençgâh", "Sazkar", "Sâzkâr", "Nevâ", "Neva Büselik", "Tahir", "Tâhir Büselik", "Hüseyni", "Hüseyni ‘Asiran", "Gülizâr", "Yegâh", "Beyâti Araban", "Muhayyer", "Muhayyer Büselik", "Gerdâniye",  "Gerdaniye Büselik", "Dilkeş Haveran", "Evc Büselik", "Irak"}, ["B -0.5", "F 1"]), 
  ({"Acem Kürdi", "Acem Asiran", "Kürdi", "Muhayyer-Kiird"}, ["B -1"]), 
  ({"Muhayyer Siinbiile", "Saba", "Saba Blselik", "Saba-Zemzeme", 
  "Bestenigar", "Şevk Efza", "Sevk-i Tarab", "Şevk ü Tarab"}, ["B -0.5", "D -0.25"]), 
  ({"Ussak", "Beyati", "Beyati- Buselik", "Isfahan", "Berte-Isfahan", "Hisar"}, ["B -0.5"]), 
  ({"Nisaburek", "Eve Ara", "Ferahnak"}, ["F 1", "C 1"]),
  ({"Suzidilara", "Mahur", "Mahur-Buselik", "Zavi*"}, ["F 0.25"]),
  ({"Nikriz", "Sehnaz"}, ["B -0.25", "C 1"]), 
  ({"Hisar-Buselik", "Suzdi"}, ["F 0.5", "G 1", "D 1"]), 
  ({"Segah", "Mistear"}, ["B -0.5","E -0.5", "F 1"]), 
  ({"Hlzzam", "Karcigar", "Beyati Araban-Buselik"}, ["B -0.5", "E -0.25", "F 1"]), 
  ({"Kurdili Hicazkar"}, ["B -1", "E -1", "A -1"]), 
  ({"Hicazkar"}, ["B -0.5", "E -0.25", "A -0.25", "F 1"]), 
  ({"Neveser"}, ["B -0.25", "E -0.25", "F 1", "C 1"]), 
  ({"Hicaz", "Hicaz Asiran", "Hicaz-Buselik"}, ["B -0.25", "F 1", "C 1"]), 
  ({"Arazbar", "Arazbar-Buselik"}, ["B -0.5", "E -0.5"]), 
  ({"Buselik-Asiran"}, ["F 1"]) 
]


def strks_to_xml(strks):
  """

  Helper. Takes strks, which is a string for key signature in the format:
  "note Ahalf-steps"

  and turns them into XML.
  """

  key_step = strks[0] #just the first letter. varname \approx strname
  key_alter = NUM_TO_KV[strks[2:]] #second til end is the number.
  key_accidental = NUM_TO_ACC[strks[2:]] #gives the right name

  xmlstr = "" #this will provide the full name
  xmlstr += "<key-step>" + key_step + "</key-step>\n"
  xmlstr += "<key-alter>" + key_alter + "</key-alter>\n"
  xmlstr += "<key-accidental>" + key_accidental + "</key-accidental>"

  return xmlstr #return the full XML.
