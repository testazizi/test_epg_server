import cv2
import numpy as np
import sys
from pathlib import Path
import glob
import os
import time
import datetime
from datetime import datetime, date , timedelta
import os.path


filename = str(sys.argv[1])
print('iframe detected:'+filename)
# iframe = cv2.imread(filename)
iframe = cv2.imread(filename)
# iframe = cv2.imread("iframes_live/"+filename)
# iframe = cv2.imread(filename)


def compare_image(image_1, image_2):
    first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match

    # taking only 10% of histogram diff, since it's less accurate than template method
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff





jingle1_1 = cv2.imread("jingles_iframes/iframe_jingle1/jingle1_1.png")
jingle1_2 = cv2.imread("jingles_iframes/iframe_jingle1/jingle1_2.png")
# jingle1_3 = cv2.imread("2021-09-13/2021-09-13_10:07:53__5563.png")

jingle2_1 = cv2.imread("jingles_iframes/iframe_jingle2/jingle2_1.png")
jingle2_2 = cv2.imread("jingles_iframes/iframe_jingle2/jingle2_2.png")

jingle3_1 = cv2.imread("iframes_live_old/index60.1648513772_59_6.png")
jingle3_2 = cv2.imread("iframes_live_old/index60.1648513772_85_6.png")
jingle3_3 = cv2.imread("iframes_live_old/index60.1648513772_86_6.png")
# jingle3 = cv2.imread("2021-09-13/2021-09-13_14:08:38__33630.png")

jingle4_1 = cv2.imread("jingles_iframes/iframe_jingle4/jingle4_1.png")
jingle4_2 = cv2.imread("jingles_iframes/iframe_jingle4/jingle4_2.png")
jingle4_3 = cv2.imread("jingles_iframes/iframe_jingle4/jingle4_3.png")
# jingle4_3 = cv2.imread("2021-09-13/2021-09-13_00:05:59__43302.png")

# jingle5_1 = cv2.imread("jingles_iframes/iframe_jingle5/jingle5_1.png")
# jingle5_2 = cv2.imread("jingles_iframes/iframe_jingle5/jingle5_2.png")
jingle5_1 = cv2.imread("iframes_live_old/index565.1648686004_144_6.png")
jingle5_2 = cv2.imread("iframes_live_old/index566.1648686010_37_6.png")
# jingle5_3 = cv2.imread("2021-09-13/2021-09-13_01:06:13__40948.png")

jingle6_1 = cv2.imread("jingles_iframes/iframe_jingle6/jingle6_1.png")
jingle6_2 = cv2.imread("jingles_iframes/iframe_jingle6/jingle6_2.png")
jingle6_3 = cv2.imread("iframes_live_old/index140.1647943665_1_3.png")
# http://167.86.88.47/jingles_detector/iframes_live/index140.1647943665_1_3.png

jingles_time = {}
jingles_time["jingle_1"] = 7
jingles_time["jingle_2"] = 7
jingles_time["jingle_3"] = 6
jingles_time["jingle_4"] = 6
jingles_time["jingle_5"] = 8
jingles_time["jingle_6"] = 6


frame_in_jingle = {}
frame_in_jingle["jingle_1"] = []
frame_in_jingle["jingle_1"].append(3)
frame_in_jingle["jingle_1"].append(4)

frame_in_jingle["jingle_2"] = []
frame_in_jingle["jingle_2"].append(2)
frame_in_jingle["jingle_2"].append(5)

frame_in_jingle["jingle_3"] = []
frame_in_jingle["jingle_3"].append(1)
frame_in_jingle["jingle_3"].append(3)

frame_in_jingle["jingle_4"] = []
frame_in_jingle["jingle_4"].append(0)
frame_in_jingle["jingle_4"].append(3)
frame_in_jingle["jingle_4"].append(4)

frame_in_jingle["jingle_5"] = []
frame_in_jingle["jingle_5"].append(1)
frame_in_jingle["jingle_5"].append(2)
frame_in_jingle["jingle_5"].append(3)

frame_in_jingle["jingle_6"] = []
frame_in_jingle["jingle_6"].append(0)
frame_in_jingle["jingle_6"].append(3)
frame_in_jingle["jingle_6"].append(3)
# frame_in_jingle["jingle_6"].append(4)

jingles_group = {}
jingles_group["jingle_1"] = []
jingles_group["jingle_1"].append(jingle1_1)
jingles_group["jingle_1"].append(jingle1_2)

jingles_group["jingle_2"] = []
jingles_group["jingle_2"].append(jingle2_1)
jingles_group["jingle_2"].append(jingle2_2)

jingles_group["jingle_3"] = []
jingles_group["jingle_3"].append(jingle3_1)
jingles_group["jingle_3"].append(jingle3_2)
jingles_group["jingle_3"].append(jingle3_3)

jingles_group["jingle_4"] = []
jingles_group["jingle_4"].append(jingle4_1)
jingles_group["jingle_4"].append(jingle4_2)
jingles_group["jingle_4"].append(jingle4_3)

jingles_group["jingle_5"] = []
jingles_group["jingle_5"].append(jingle5_1)
jingles_group["jingle_5"].append(jingle5_2)

jingles_group["jingle_6"] = []
jingles_group["jingle_6"].append(jingle6_1)
jingles_group["jingle_6"].append(jingle6_2)
jingles_group["jingle_6"].append(jingle6_3)



i=0
last_frame_name = 'none'
last_frame_time = datetime.now()
now = datetime.now()
now_string = now.strftime("%Y-%m-%d %H:%M:%S")
now_string_api = str(now_string).replace(" ", "_")
jing_n = 0




# print('iframe detected:'+filename)
# segment_file = "2m_hls/"+str(filename.split("_")[0])+".ts"
# print("segment_file:"+segment_file)
# lenght_seg = int(str(filename.split("_")[2]).replace(".png",""))
# frame_in_seg = int(filename.split("_")[1])
# time_in_seg = lenght_seg - int(float(frame_in_seg)/25)

for jingles in jingles_group:
    jing_n +=1
    jingle_name = jingles
    index = 0
    for jingle in jingles_group[jingles]:
        # indexo = 1
        print(str(compare_image(jingle,iframe)))
        print(str(jingles))

        if float(compare_image(jingle,iframe)) < 0.1 and os.path.exists("iframes_live/"+filename):
            os.system("cp iframes_live/"+filename+" jingles_found/")
            # print(str(jingles)+str(index))
            # print(str(compare_image(jingle,iframe)))

            start_J_end_seg = int(jingles_time[jingle_name]) - frame_in_jingle[jingle_name][index]
            now_start = datetime.now() - timedelta(seconds=time_in_seg) + timedelta(seconds=start_J_end_seg)
            now_start_string = now_start.strftime("%Y-%m-%d %H:%M:%S")

            end_J_start_seg = int(frame_in_jingle[jingle_name][index])
            now_end = datetime.now() - timedelta(seconds=time_in_seg) - timedelta(seconds=end_J_start_seg)
            now_end_string = now_end.strftime("%Y-%m-%d %H:%M:%S")


            now_string_api = str(now_start_string).replace(" ", "_")

            file1 = open('last_live_jingle.txt', 'r')

            if os.stat("last_live_jingle.txt").st_size == 0:
                print("================= Jingle Start at "+now_start_string)
                check = now_start_string+" --- "+jingle_name
                with open("logs.txt",'a') as g:
                    g.write("================"+"\n")
                    g.write("Jingle "+jingle_name+" number "+str(index)+" detected at"+now_start_string+"\n")
                    g.write("================"+"\n")
                    os.system("python3 adspot_api.py "+now_string_api+" start jingle")
                    g.close()
                os.system("> last_live_jingle.txt")
                with open("last_live_jingle.txt",'w') as f:
                    f.write(now_start_string+" --- "+jingle_name+" --- start"+"\n")
                    f.close()
                    last_frame_time = now_start_string
                    last_frame_name = jingle_name
            else:


                for line in file1:
                    pass
                last_line = line
                if "---" in line:

                    line_arr = line.split(' --- ')
                    airtime0 = line_arr[0]
                    print(line_arr[0])
                    last_frame_name = line_arr[1]
                    last_role = line_arr[2]
                    last_airtime = datetime.strptime(airtime0, '%Y-%m-%d %H:%M:%S')

                    duration_since_last = now_end - last_airtime
                    duration_since_last = duration_since_last.total_seconds()
                    print("duration:"+str(duration_since_last))

                    if round(duration_since_last) < 8 and last_frame_name == jingle_name:
                        print("same jingle")

                    elif round(duration_since_last) > 5 and round(duration_since_last) < 600 and "start" in last_role :
                        adbreak_channel = "2M"
                        adbreak_start_at = last_airtime
                        adbreak_duration = int(duration_since_last)
                        with open("logs.txt",'a') as g:
                            g.write("================"+"\n")
                            g.write("call to python functions  ")
                            g.write("Jingle "+jingle_name+" number "+str(index)+" detected at"+now_string+"\n")
                            g.write("duration: "+str(round(duration_since_last))+"\n")
                            g.write("================"+"\n")
                            g.close()

                        os.system("> last_live_jingle.txt")
                        with open("last_live_jingle.txt",'w') as f:
                            f.write(now_start_string+" --- "+jingle_name+" --- end"+"\n")
                            f.close()
                        print("python3 api_request.py 1 "+now_string_api+" "+str(round(duration_since_last)))
                        os.system("python3 api_request.py 1 "+now_string_api+" "+str(round(duration_since_last))+" "+jingle_name)
                        print("call to python functions =======================================")

                    elif round(duration_since_last) > 800 :
                        print("================= Jingle Start at "+now_start_string)
                        check = now_start_string+" --- "+jingle_name
                        os.system("python3 adspot_api.py "+now_string_api+" start jingle")

                        with open("logs.txt",'a') as g:
                            g.write("================"+"\n")
                            g.write("Jingle Start at   ")
                            g.write("Jingle "+jingle_name+" number "+str(index)+" detected at"+now_start_string+"\n")
                            g.write("================"+"\n")
                            g.close()
                        os.system("> last_live_jingle.txt")

                        with open("last_live_jingle.txt",'w') as f:
                            f.write(now_start_string+" --- "+jingle_name+" --- start"+"\n")
                            f.close()
                            last_frame_time = now_start_string
                            last_frame_name = jingle_name

                    else:
                                # python send msg
                        print("================= Jingle Start at "+now_start_string)
                        check = now_start_string+" --- "+jingle_name
                        os.system("python3 adspot_api.py "+now_string_api+" start jingle")

                        with open("logs.txt",'a') as g:
                            g.write("================"+"\n")
                            g.write("Jingle Start at   ")
                            g.write("Jingle "+jingle_name+" number "+str(index)+" detected at"+now_start_string+"\n")
                            g.write("================"+"\n")
                            g.close()
                        with open("last_live_jingle.txt",'w') as f:
                            f.write(now_start_string+" --- "+jingle_name+" --- start"+"\n")
                            f.close()
                            last_frame_time = now_start_string
                            last_frame_name = jingle_name

        index+=1


blue_frame = cv2.imread("iframes_live_old/index9.1648311863_48_6.png")
sabahiat_2m = cv2.imread("shows_iframes/sabahiat_2m/start/img1.png")
moujaz_riyadi = cv2.imread("shows_iframes/moujaz_riyadi/start/img1.png")
lilmatbakh_nojom = cv2.imread("shows_iframes/lilmatbakh_nojom/start/img1.png")
kaifa_alhal = cv2.imread("shows_iframes/kaifa_alhal/start/index425.1653372603_15_6.png")
journal_amazigh = cv2.imread("shows_iframes/journal_amazigh/start/img1.png")
info_soir = cv2.imread("shows_iframes/info_soir/start/img1.png")
al_wa3d = cv2.imread("shows_iframes/al_wa3d/start/img1.png")
info_soir = cv2.imread("shows_iframes/info_soir/start/img1.png")
que_du_sport = cv2.imread("shows_iframes/que_du_sport/start/img2.png")

carrefour = cv2.imread("iframes_live_old/index210.1648338262_65_6.png")
orange = cv2.imread("iframes_live_old/index209.1648338255_73_6.png")


if float(compare_image(blue_frame,iframe)) < 0.1 and os.path.exists("iframes_live_old/"+filename):
    print("blue_frame" +str(compare_image(blue_frame,iframe)))
    print("python3 adspot_api.py "+now_string_api+" Blue_Frame")
    os.system("python3 adspot_api.py "+now_string_api+" Blue_Frame")

if float(compare_image(sabahiat_2m,iframe)) < 0.1 :

    print("python3 adspot_api.py "+now_string_api+" sabahiat_2m")
    os.system("python3 adspot_api.py "+now_string_api+" Sabahiat_2M")

print(str(compare_image(info_soir,iframe)))

if float(compare_image(info_soir,iframe)) < 0.1:
        print(str(compare_image(info_soir,iframe)))
        os.system("python3 adspot_api.py "+now_string_api+" info_soir")

if float(compare_image(que_du_sport,iframe)) < 0.1:
    print(str(compare_image(moujaz_riyadi,iframe)))
    os.system("python3 adspot_api.py "+now_string_api+" que_du_sport")
