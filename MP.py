import texttable as tt
import pandas as pd
import numpy as np
tab1 = tt.Texttable()
tab2 = tt.Texttable()
tab3 = tt.Texttable()
tab4 = tt.Texttable()
tab5 = tt.Texttable()
tab6 = tt.Texttable()
tab7 = tt.Texttable()
tab8 = tt.Texttable()

not_recom, recommend, very_recom, priority, spec_prior = [],[],[],[],[]

#parents
not_rec_usual ,not_rec_pretentious ,not_rec_great_pret = 0,0,0
rec_usual ,rec_pretentious ,rec_great_pret = 0,0,0
ver_rec_usual ,ver_rec_pretentious ,ver_rec_great_pret = 0,0,0
pri_usual ,pri_pretentious ,pri_great_pret = 0,0,0
spe_usual ,spe_pretentious ,spe_great_pret = 0,0,0
#has_nurs
not_pro , not_less_pro , not_impro , not_crit ,not_ver_crit = 0,0,0,0,0
rec_pro , rec_less_pro , rec_impro , rec_crit ,rec_ver_crit = 0,0,0,0,0
ver_pro , ver_less_pro , ver_impro , ver_crit ,ver_ver_crit = 0,0,0,0,0
pri_pro , pri_less_pro , pri_impro , pri_crit ,pri_ver_crit = 0,0,0,0,0
spe_pro , spe_less_pro , spe_impro , spe_crit ,spe_ver_crit = 0,0,0,0,0
#form
not_com , not_compd , not_incom , not_fost = 0,0,0,0
rec_com , rec_compd , rec_incom , rec_fost = 0,0,0,0
ver_com , ver_compd , ver_incom , ver_fost = 0,0,0,0
pri_com , pri_compd , pri_incom , pri_fost = 0,0,0,0
spe_com , spe_compd , spe_incom , spe_fost = 0,0,0,0
#children
not_1 , not_2 , not_3 , not_more = 0,0,0,0
rec_1 , rec_2 , rec_3 , rec_more = 0,0,0,0
ver_1 , ver_2 , ver_3 , ver_more = 0,0,0,0
pri_1 , pri_2 , pri_3 , pri_more = 0,0,0,0
spe_1 , spe_2 , spe_3 , spe_more = 0,0,0,0
#housing
not_conv , not_less_con , not_hous_crit = 0,0,0
rec_conv , rec_less_con , rec_hous_crit = 0,0,0
ver_conv , ver_less_con , ver_hous_crit = 0,0,0
pri_conv , pri_less_con , pri_hous_crit = 0,0,0
spe_conv , spe_less_con , spe_hous_crit = 0,0,0
#finance
not_convt , not_inconv = 0,0
rec_convt , rec_inconv = 0,0
ver_convt , ver_inconv = 0,0
pri_convt , pri_inconv = 0,0
spe_convt , spe_inconv = 0,0
#social
not_nonpr , not_slipr , not_probl = 0,0,0
rec_nonpr , rec_slipr , rec_probl = 0,0,0
ver_nonpr , ver_slipr , ver_probl = 0,0,0
pri_nonpr , pri_slipr , pri_probl = 0,0,0
spe_nonpr , spe_slipr , spe_probl = 0,0,0
#health
not_rec , not_prior , not_notrec = 0,0,0
rec_rec , rec_prior , rec_notrec = 0,0,0
ver_rec , ver_prior , ver_notrec = 0,0,0
pri_rec , pri_prior , pri_notrec = 0,0,0
spe_rec , spe_prior , spe_notrec = 0,0,0

with open("nursery.data","r")as file :
	data = file.readlines()
	for line in data:
		word = line.split(",")
		if line == "\n":
			continue
		if (word[8]=="not_recom\n"):
			not_recom.append(word)
		elif (word[8]=="recommend\n"):
			recommend.append(word)
		elif (word[8] == "very_recom\n"):
			very_recom.append(word)
		elif (word[8] == "priority\n"):
			priority.append(word)
		elif (word[8] == "spec_prior\n"):
			spec_prior.append(word)
	#print(not_recom)
	print("not_recom ->",len(not_recom))
	print((len(not_recom)/12960),"%")
	#print(recommend)
	print("recommend ->",len(recommend))
	print((len(recommend)/12960),"%")
	#print(very_recom)
	print("very_recom ->",len(very_recom))
	print((len(very_recom)/12960),"%")
	#print(priority)
	print("priority ->",len(priority))
	print((len(priority)/12960),"%")
	#print(spec_prior)
	print("spec_prior ->",len(spec_prior))
	print((len(spec_prior)/12960),"%")
	
not_recom_arr = [[0 for i in range(8)] for j in range(len(not_recom))]
for i in range(len(not_recom_arr)):
	for j in range(8):
		not_recom_arr[i][j]= not_recom[i][j]
		# parents:
		if(j==0):
			if (not_recom_arr[i][j]=='usual'):
				not_rec_usual = not_rec_usual + 1
			if (not_recom_arr[i][j]=='pretentious'):
				not_rec_pretentious = not_rec_pretentious + 1
			if (not_recom_arr[i][j]=='great_pret'):
				not_rec_great_pret = not_rec_great_pret + 1
		# has_nurs
		if(j==1):
			if(not_recom_arr[i][j]=='proper'):
				not_pro = not_pro + 1
			if (not_recom_arr[i][j] == "less_proper"):
				not_less_pro = not_less_pro + 1
			if (not_recom_arr[i][j] == 'improper'):
				not_impro = not_impro + 1
			if (not_recom_arr[i][j] == 'critical'):
				not_crit = not_crit + 1
			if (not_recom_arr[i][j] == 'very_crit'):
				not_ver_crit= not_ver_crit + 1
		# form
		if(j==2):
			if (not_recom_arr[i][j] == 'complete'):
				not_com = not_com + 1
			if (not_recom_arr[i][j] == "completed"):
				not_compd = not_compd + 1
			if (not_recom_arr[i][j] == 'incomplete'):
				not_incom = not_incom + 1
			if (not_recom_arr[i][j] == 'foster'):
				not_fost = not_fost + 1
		# childern
		if(j==3):
			if (not_recom_arr[i][j] == '1'):
				not_1 = not_1 + 1
			if (not_recom_arr[i][j] == "2"):
				not_2 = not_2 + 1
			if (not_recom_arr[i][j] == '3'):
				not_3 = not_3 + 1
			if (not_recom_arr[i][j] == 'more'):
				not_more = not_more + 1
		#housing
		if(j==4):
			if (not_recom_arr[i][j] == 'convenient'):
				not_conv = not_conv + 1
			if (not_recom_arr[i][j] == 'less_conv'):
				not_less_con = not_less_con + 1
			if (not_recom_arr[i][j] == 'critical'):
				not_hous_crit = not_hous_crit + 1
		#finance
		if(j==5):
			if (not_recom_arr[i][j] == 'inconv'):
				not_inconv = not_inconv + 1
			if (not_recom_arr[i][j] == 'convenient'):
				not_convt = not_convt + 1
		#social
		if(j==6):
			if (not_recom_arr[i][j] == 'nonprob'):
				not_nonpr = not_nonpr + 1
			if (not_recom_arr[i][j] == 'slightly_prob'):
				not_slipr = not_slipr + 1
			if (not_recom_arr[i][j] == 'problematic'):
				not_probl = not_probl + 1
		#health
		if(j==7):
			if (not_recom_arr[i][j] == 'recommended'):
				not_rec = not_rec + 1
			if (not_recom_arr[i][j] == 'priority'):
				not_prior = not_prior + 1
			if (not_recom_arr[i][j] == 'not_recom'):
				not_notrec = not_notrec + 1

recommend_arr = [[0 for i in range(8)] for j in range(len(recommend))]
for i in range(len(recommend)):
	for j in range(8):
		recommend_arr[i][j]=recommend[i][j]
		# parents:
		if(j==0):
			if (recommend_arr[i][j] == 'usual'):
				rec_usual = rec_usual + 1
			if (recommend_arr[i][j] == 'pretentious'):
				rec_pretentious = rec_pretentious + 1
			if (recommend_arr[i][j] == 'great_pret'):
				rec_great_pret = rec_great_pret + 1
		# has_nurs
		if(j==1):
			if (recommend_arr[i][j]== 'proper'):
				rec_pro = rec_pro + 1
			if (recommend_arr[i][j] == 'less_proper'):
				rec_less_pro = rec_less_pro + 1
			if (recommend_arr[i][j] == 'improper'):
				rec_impro = rec_impro + 1
			if (recommend_arr[i][j] == 'critical'):
				rec_crit = rec_crit + 1
			if (recommend_arr[i][j] == 'very_crit'):
				rec_ver_crit = rec_ver_crit + 1
		#form
		if(j==2):
			if (recommend_arr[i][j]== 'complete'):
				rec_com = rec_com + 1
			if (recommend_arr[i][j] == 'completed'):
				rec_compd = rec_compd + 1
			if (recommend_arr[i][j] == 'incomplete'):
				rec_incom = rec_incom + 1
			if (recommend_arr[i][j] == 'foster'):
				rec_fost = rec_fost + 1
		# childern
		if(j==3):
			if (recommend_arr[i][j] == '1'):
				rec_1 = rec_1 + 1
			if (recommend_arr[i][j] == "2"):
				rec_2 = rec_2 + 1
			if (recommend_arr[i][j] == '3'):
				rec_3 = rec_3 + 1
			if (recommend_arr[i][j] == 'more'):
				rec_more = rec_more + 1
		#housing
		if(j==4):
			if (recommend_arr[i][j] == 'convenient'):
				rec_conv = rec_conv + 1
			if (recommend_arr[i][j] == 'less_conv'):
				rec_less_con = rec_less_con + 1
			if (recommend_arr[i][j] == 'critical'):
				rec_hous_crit = rec_hous_crit + 1
		# finance
		if(j==5):
			if (recommend_arr[i][j] == 'inconv'):
				rec_inconv = rec_inconv + 1
			if (recommend_arr[i][j] == 'convenient'):
				rec_convt = rec_convt + 1
		#social
		if(j==6):
			if (recommend_arr[i][j] == 'nonprob'):
				rec_nonpr = rec_nonpr + 1
			if (recommend_arr[i][j] == 'slightly_prob'):
				rec_slipr = rec_slipr + 1
			if (recommend_arr[i][j] == 'problematic'):
				rec_probl = rec_probl + 1
		#health
		if (j == 7):
			if (recommend_arr[i][j] == 'recommended'):
				rec_rec = rec_rec + 1
			if (recommend_arr[i][j] == 'priority'):
				rec_prior = rec_prior + 1
			if (recommend_arr[i][j] == 'not_recom'):
				rec_notrec = rec_notrec + 1

very_recom_arr = [[0 for i in range(8)] for j in range(len(very_recom))]
for i in range(len(very_recom)):
	for j in range(8):
		very_recom_arr[i][j]=very_recom[i][j]
		# parents:
		if(j==0):
			if (very_recom_arr[i][j] == 'usual'):
				ver_rec_usual = ver_rec_usual + 1
			if (very_recom_arr[i][j] == 'pretentious'):
				ver_rec_pretentious = ver_rec_pretentious + 1
			if (very_recom_arr[i][j] == 'great_pret'):
				ver_rec_great_pret = ver_rec_great_pret + 1
		# has_nurs
		if(j==1):
			if (very_recom_arr[i][j] == 'proper'):
				ver_pro = ver_pro + 1
			if (very_recom_arr[i][j] == 'less_proper'):
				ver_less_pro = ver_less_pro + 1
			if (very_recom_arr[i][j] == 'improper'):
				ver_impro = ver_impro + 1
			if (very_recom_arr[i][j] == 'critical'):
				ver_crit = ver_crit + 1
			if (very_recom_arr[i][j] == 'very_crit'):
				ver_ver_crit = ver_ver_crit + 1
		# form
		if (j == 2):
			if (very_recom_arr[i][j]  == 'complete'):
				ver_com = ver_com + 1
			if (very_recom_arr[i][j]  == "completed"):
				ver_compd = ver_compd + 1
			if (very_recom_arr[i][j]  == 'incomplete'):
				ver_incom = ver_incom + 1
			if (very_recom_arr[i][j]  == 'foster'):
				ver_fost = ver_fost + 1
		# childern
		if(j==3):
			if (very_recom_arr[i][j] == '1'):
				ver_1 = ver_1 + 1
			if (very_recom_arr[i][j] == "2"):
				ver_2 = ver_2 + 1
			if (very_recom_arr[i][j] == '3'):
				ver_3 = ver_3 + 1
			if (very_recom_arr[i][j] == 'more'):
				ver_more = ver_more + 1
		#housing
		if(j==4):
			if (very_recom_arr[i][j] == 'convenient'):
				ver_conv = ver_conv + 1
			if (very_recom_arr[i][j] == 'less_conv'):
				ver_less_con = ver_less_con + 1
			if (very_recom_arr[i][j] == 'critical'):
				ver_hous_crit = ver_hous_crit + 1
		# finance
		if(j==5):
			if (very_recom_arr[i][j] == 'inconv'):
				ver_inconv = ver_inconv + 1
			if (very_recom_arr[i][j] == 'convenient'):
				ver_convt = ver_convt + 1
		# social
		if (j == 6):
			if (very_recom_arr[i][j] == 'nonprob'):
				ver_nonpr = ver_nonpr + 1
			if (very_recom_arr[i][j] == 'slightly_prob'):
				ver_slipr = ver_slipr + 1
			if (very_recom_arr[i][j] == 'problematic'):
				ver_probl = ver_probl + 1
		# health
		if (j == 7):
			if (very_recom_arr[i][j] == 'recommended'):
				ver_rec = ver_rec + 1
			if (very_recom_arr[i][j] == 'priority'):
				ver_prior = ver_prior + 1
			if (very_recom_arr[i][j] == 'not_recom'):
				ver_notrec = ver_notrec + 1
				
priority_arr = [[0 for i in range(8)] for j in range(len(priority))]
for i in range(len(priority)):
	for j in range(8):
		priority_arr[i][j] = priority[i][j]
		# parents:
		if(j==0):
			if (priority_arr[i][j] == 'usual'):
				pri_usual = pri_usual + 1
			if (priority_arr[i][j] == 'pretentious'):
				pri_pretentious = pri_pretentious + 1
			if (priority_arr[i][j] == 'great_pret'):
				pri_great_pret = pri_great_pret + 1
		# has_nurs
		if(j==1):
			if (priority_arr[i][j] == 'proper'):
				pri_pro = pri_pro + 1
			if (priority_arr[i][j] == 'less_proper'):
				pri_less_pro = pri_less_pro + 1
			if (priority_arr[i][j] == 'improper'):
				pri_impro = pri_impro + 1
			if (priority_arr[i][j] == 'critical'):
				pri_crit = pri_crit + 1
			if (priority_arr[i][j] == 'very_crit'):
				pri_ver_crit = pri_ver_crit + 1
		# form
		if(j==2):
			if (priority_arr[i][j] == 'complete'):
				pri_com = pri_com + 1
			if (priority_arr[i][j] == "completed"):
				pri_compd = pri_compd + 1
			if (priority_arr[i][j] == 'incomplete'):
				pri_incom = pri_incom + 1
			if (priority_arr[i][j] == 'foster'):
				pri_fost = pri_fost + 1
		# childern
		if(j==3):
			if (priority_arr[i][j] == '1'):
				pri_1 = pri_1 + 1
			if (priority_arr[i][j] == "2"):
				pri_2 = pri_2 + 1
			if (priority_arr[i][j] == '3'):
				pri_3 = pri_3 + 1
			if (priority_arr[i][j] == 'more'):
				pri_more = pri_more + 1
		#housing
		if(j==4):
			if (priority_arr[i][j] == 'convenient'):
				pri_conv = pri_conv + 1
			if (priority_arr[i][j] == 'less_conv'):
				pri_less_con = pri_less_con + 1
			if (priority_arr[i][j] == 'critical'):
				pri_hous_crit = pri_hous_crit + 1
		# finance
		if(j==5):
			if (priority_arr[i][j] == 'inconv'):
				pri_inconv = pri_inconv + 1
			if (priority_arr[i][j] == 'convenient'):
				pri_convt = pri_convt + 1
		# social
		if (j == 6):
			if (priority_arr[i][j] == 'nonprob'):
				pri_nonpr = pri_nonpr + 1
			if (priority_arr[i][j] == 'slightly_prob'):
				pri_slipr = pri_slipr + 1
			if (priority_arr[i][j] == 'problematic'):
				pri_probl = pri_probl + 1
		# health
		if (j == 7):
			if (priority_arr[i][j] == 'recommended'):
				pri_rec = pri_rec + 1
			if (priority_arr[i][j] == 'priority'):
				pri_prior = pri_prior + 1
			if (priority_arr[i][j] == 'not_recom'):
				pri_notrec = pri_notrec + 1

spec_prior_arr = [[0 for i in range(8)] for j in range(len(spec_prior))]
for i in range(len(spec_prior)):
	for j in range(8):
		spec_prior_arr[i][j] = spec_prior[i][j]
		# parents:
		if(j==0):
			if (spec_prior_arr[i][j] == 'usual'):
				spe_usual = spe_usual + 1
			if (spec_prior_arr[i][j] == 'pretentious'):
				spe_pretentious = spe_pretentious + 1
			if (spec_prior_arr[i][j] == 'great_pret'):
				spe_great_pret = spe_great_pret + 1
		# has_nurs
		if (j==1):
			if (spec_prior_arr[i][j] == 'proper'):
				spe_pro = spe_pro + 1
			if (spec_prior_arr[i][j] == 'less_proper'):
				spe_less_pro = spe_less_pro + 1
			if (spec_prior_arr[i][j]== 'improper'):
				spe_impro = spe_impro + 1
			if (spec_prior_arr[i][j] == 'critical'):
				spe_crit = spe_crit + 1
			if (spec_prior_arr[i][j] == 'very_crit'):
				spe_ver_crit = spe_ver_crit + 1
		# form
		if(j==2):
			if (spec_prior_arr[i][j] == 'complete'):
				spe_com = spe_com + 1
			if (spec_prior_arr[i][j] == "completed"):
				spe_compd = spe_compd + 1
			if (spec_prior_arr[i][j] == 'incomplete'):
				spe_incom = spe_incom + 1
			if (spec_prior_arr[i][j] == 'foster'):
				spe_fost = spe_fost + 1
		# childern
		if(j==3):
			if (spec_prior_arr[i][j] == '1'):
				spe_1 = spe_1 + 1
			if (spec_prior_arr[i][j] == "2"):
				spe_2 = spe_2 + 1
			if (spec_prior_arr[i][j] == '3'):
				spe_3 = spe_3 + 1
			if (spec_prior_arr[i][j] == 'more'):
				spe_more = spe_more + 1
		#housing
		if(j==4):
			if (spec_prior_arr[i][j] == 'convenient'):
				spe_conv = spe_conv + 1
			if (spec_prior_arr[i][j] == 'less_conv'):
				spe_less_con = spe_less_con + 1
			if (spec_prior_arr[i][j] == 'critical'):
				spe_hous_crit = spe_hous_crit + 1
		# finance
		if(j==5):
			if (spec_prior_arr[i][j] == 'inconv'):
				spe_inconv = spe_inconv + 1
			if (spec_prior_arr[i][j] == 'convenient'):
				spe_convt = spe_convt + 1
		# social
		if (j == 6):
			if (spec_prior_arr[i][j] == 'nonprob'):
				spe_nonpr = spe_nonpr + 1
			if (spec_prior_arr[i][j] == 'slightly_prob'):
				spe_slipr = spe_slipr + 1
			if (spec_prior_arr[i][j] == 'problematic'):
				spe_probl = spe_probl + 1
		# health
		if (j == 7):
			if (spec_prior_arr[i][j] == 'recommended'):
				spe_rec = spe_rec + 1
			if (spec_prior_arr[i][j] == 'priority'):
				spe_prior = spe_prior + 1
			if (spec_prior_arr[i][j] == 'not_recom'):
				spe_notrec = spe_notrec + 1


freq = input("What Is Freuency Table Attribute ? ")
print("                              FREQUENCY TABLE ")
#parents frequency
headings = ['Patents', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab1.header(headings)
names = ['usual', 'pretentious', 'great_pret']
not_recommend = [not_rec_usual, not_rec_pretentious, not_rec_great_pret]
recommen = [rec_usual, rec_pretentious, rec_great_pret]
veryrecom = [ver_rec_usual, ver_rec_pretentious, ver_rec_great_pret]
priorit = [pri_usual, pri_pretentious, pri_great_pret]
specprior = [spe_usual, spe_pretentious, spe_great_pret]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab1.add_row(row)
#has_nurs frequency
headings = ['Has_nurs', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab2.header(headings)
names = ['proper', 'less_proper', 'improper', 'critical', 'very_crit']
not_recommend = [not_pro, not_less_pro, not_impro, not_crit,not_ver_crit]
recommen = [rec_pro, rec_less_pro, rec_impro, rec_crit, rec_ver_crit]
veryrecom = [ver_pro, ver_less_pro, ver_impro, ver_crit, ver_ver_crit]
priorit = [pri_pro, pri_less_pro, pri_impro, pri_crit, pri_ver_crit]
specprior = [spe_pro, spe_less_pro, spe_impro, spe_crit, spe_ver_crit]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab2.add_row(row)
#form frequency
headings = ['Form', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab3.header(headings)
names = ['complete', 'completed', 'incomplete', 'foster']
not_recommend = [not_com, not_compd, not_incom, not_fost]
recommen = [rec_com, rec_compd, rec_incom, rec_fost]
veryrecom = [ver_com, ver_compd, ver_incom, ver_fost]
priorit = [pri_com, pri_compd, pri_incom, pri_fost]
specprior = [spe_com, spe_compd, spe_incom, spe_fost]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab3.add_row(row)
#children frequency
headings = ['Children', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab4.header(headings)
names = ['one', 'two', 'three', 'more']
not_recommend = [not_1, not_2, not_3, not_more]
recommen = [rec_1, rec_2, rec_3, rec_more]
veryrecom = [ver_1, ver_2, ver_3, ver_more]
priorit = [pri_1, pri_2, pri_3, pri_more]
specprior = [spe_1, spe_2, spe_3, spe_more]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab4.add_row(row)
#housing frequency
headings = ['Housing', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab5.header(headings)
names = ['convenient', 'less_conv', 'critical']
not_recommend = [not_conv, not_less_con, not_hous_crit]
recommen = [rec_conv, rec_less_con, rec_hous_crit]
veryrecom = [ver_conv, ver_less_con, ver_hous_crit]
priorit = [pri_conv, pri_less_con, pri_hous_crit]
specprior =[spe_conv, spe_less_con, spe_hous_crit]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab5.add_row(row)
#finance frequency
headings = ['Finance', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab6.header(headings)
names = ['convenient', 'inconv']
not_recommend = [not_convt, not_inconv]
recommen = [rec_convt, rec_inconv]
veryrecom = [ver_convt, ver_inconv]
priorit = [pri_convt, pri_inconv ]
specprior = [spe_convt, spe_inconv]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab6.add_row(row)
#social frequency
headings = ['Social', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab7.header(headings)
names = ['nonprob', 'slightly_prob', 'problematic']
not_recommend = [not_nonpr, not_slipr, not_probl]
recommen = [rec_nonpr, rec_slipr, rec_probl]
veryrecom = [ver_nonpr, ver_slipr, ver_probl]
priorit = [pri_nonpr, pri_slipr, pri_probl]
specprior = [spe_nonpr, spe_slipr, spe_probl]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab7.add_row(row)
#health frequency
headings = ['Health', 'Not_Recom', 'Recommend', 'very_Recom', 'Priority', 'Spec_Prior']
tab8.header(headings)
names = ['recommended', 'priority', 'not_recom']
not_recommend = [not_rec, not_prior, not_notrec]
recommen = [rec_rec, rec_prior, rec_notrec]
veryrecom = [ver_rec, ver_prior, ver_notrec]
priorit = [pri_rec, pri_prior, pri_notrec]
specprior = [spe_rec, spe_prior, spe_notrec]
for row in zip(names, not_recommend, recommen, veryrecom, priorit, specprior):
	tab8.add_row(row)
#parents likelihood
not_recommend = [(not_rec_usual/len(not_recom_arr)), (not_rec_pretentious/len(not_recom_arr)), (not_rec_great_pret/len(not_recom_arr)),]
recommen = [(rec_usual/len(recommend_arr)),(rec_pretentious/len(recommend_arr)), (rec_great_pret/len(recommend_arr))]
veryrecom = [(ver_rec_usual/len(very_recom_arr)), (ver_rec_pretentious/len(very_recom_arr)),(ver_rec_great_pret/len(very_recom_arr))]
priorit = [(pri_usual/len(priority_arr)), (pri_pretentious/len(priority_arr)), (pri_great_pret/len(priority_arr))]
specprior = [(spe_usual/len(spec_prior_arr)), (spe_pretentious/len(spec_prior_arr)), (spe_great_pret/len(spec_prior_arr))]
# Rezq
#pandas
parents_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                           columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                           index=['usual','pretentious','great_pret'])
#has_nurs likelihood
not_recommend = [(not_pro/len(not_recom_arr)), (not_less_pro/len(not_recom_arr)), (not_impro/len(not_recom_arr)), (not_crit/len(not_recom_arr)),(not_ver_crit/len(not_recom_arr))]
recommen = [(rec_pro/len(recommend_arr)), (rec_less_pro/len(recommend_arr)), (rec_impro/len(recommend_arr)), (rec_crit/len(recommend_arr)),(rec_ver_crit/len(recommend_arr))]
veryrecom = [(ver_pro/len(very_recom_arr)), (ver_less_pro/len(very_recom_arr)), (ver_impro/len(very_recom_arr)), (ver_crit/len(very_recom_arr)), (ver_ver_crit/len(very_recom_arr))]
priorit = [(pri_pro/len(priority_arr)), (pri_less_pro/len(priority_arr)), (pri_impro/len(priority_arr)), (pri_crit/len(priority_arr)), (pri_ver_crit/len(priority_arr))]
specprior = [(spe_pro/len(spec_prior_arr)), (spe_less_pro/len(spec_prior_arr)), (spe_impro/len(spec_prior_arr)), (spe_crit/len(spec_prior_arr)), (spe_ver_crit/len(spec_prior_arr))]
#pandas
hasnurs_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['proper', 'less_proper', 'improper','critical','very_crit'])
#form likelihood
not_recommend = [(not_com/len(not_recom_arr)), (not_compd/len(not_recom_arr)), (not_incom/len(not_recom_arr)), (not_fost/len(not_recom_arr))]
recommen = [(rec_com/len(recommend_arr)), (rec_compd/len(recommend_arr)), (rec_incom/len(recommend_arr)), (rec_fost/len(recommend_arr))]
veryrecom = [(ver_com/len(very_recom_arr)), (ver_compd/len(very_recom_arr)), (ver_incom/len(very_recom_arr)), (ver_fost/len(very_recom_arr))]
priorit = [(pri_com/len(priority_arr)), (pri_compd/len(priority_arr)), (pri_incom/len(priority_arr)), (pri_fost/len(priority_arr))]
specprior = [(spe_com/len(spec_prior_arr)), (spe_compd/len(spec_prior_arr)), (spe_incom/len(spec_prior_arr)),(spe_fost/len(spec_prior_arr))]
# pandas
form_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['complete', 'completed', 'incomplete', 'foster'])
#children likelihood
not_recommend = [(not_1/len(not_recom_arr)), (not_2/len(not_recom_arr)), (not_3/len(not_recom_arr)), (not_more/len(not_recom_arr))]
recommen = [(rec_1/len(recommend_arr)), (rec_2/len(recommend_arr)), (rec_3/len(recommend_arr)), (rec_more/len(recommend_arr))]
veryrecom = [(ver_1/len(very_recom_arr)), (ver_2/len(very_recom_arr)), (ver_3/len(very_recom_arr)), (ver_more/len(very_recom_arr))]
priorit = [(pri_1/len(priority_arr)), (pri_2/len(priority_arr)), (pri_3/len(priority_arr)), (pri_more/len(priority_arr))]
specprior = [(spe_1/len(spec_prior_arr)), (spe_2/len(spec_prior_arr)), (spe_3/len(spec_prior_arr)), (spe_more/len(spec_prior_arr))]
# pandas
children_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['1', '2', '3', 'more'])
#housing likelihood
not_recommend = [(not_conv/len(not_recom_arr)), (not_less_con/len(not_recom_arr)), (not_hous_crit/len(not_recom_arr))]
recommen = [(rec_conv/len(recommend_arr)), (rec_less_con/len(recommend_arr)), (rec_hous_crit/len(recommend_arr))]
veryrecom = [(ver_conv/len(very_recom_arr)) , (ver_less_con/len(very_recom_arr)), (ver_hous_crit/len(very_recom_arr))]
priorit = [(pri_conv/len(priority_arr)), (pri_less_con/len(priority_arr)), (pri_hous_crit/len(priority_arr))]
specprior = [(spe_conv/len(spec_prior_arr)), (spe_less_con/len(spec_prior_arr)), (spe_hous_crit/len(spec_prior_arr))]
# pandas
housing_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['convenient', 'less_conv', 'critical'])
#finance likelihod
not_recommend = [(not_convt/len(not_recom_arr)), (not_inconv/len(not_recom_arr))]
recommen = [(rec_convt/len(recommend_arr)), (rec_inconv/len(recommend_arr))]
veryrecom = [(ver_convt/len(very_recom_arr)), (ver_inconv/len(very_recom_arr))]
priorit = [(pri_convt/len(priority_arr)), (pri_inconv/len(priority_arr))]
specprior = [(spe_convt/len(spec_prior_arr)), (spe_inconv/len(spec_prior_arr))]
# pandas
finance_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['convenient', 'inconv'])
#social likelihood
not_recommend = [(not_nonpr/len(not_recom_arr)), (not_slipr/len(not_recom_arr)), (not_probl/len(not_recom_arr))]
recommen = [(rec_nonpr/len(recommend_arr)), (rec_slipr/len(recommend_arr)), (rec_probl/len(recommend_arr))]
veryrecom = [(ver_nonpr/len(very_recom_arr)), (ver_slipr/len(very_recom_arr)), (ver_probl/len(very_recom_arr))]
priorit = [(pri_nonpr/len(priority_arr)), (pri_slipr/len(priority_arr)), (pri_probl/len(priority_arr))]
specprior = [(spe_nonpr/len(spec_prior_arr)), (spe_slipr/len(spec_prior_arr)), (spe_probl/len(spec_prior_arr))]
# pandas
social_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                            columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                            index=['nonprob', 'slightly_prob', 'problematic'])
#health likelihood
not_recommend = [(not_rec/len(not_recom_arr)), (not_prior/len(not_recom_arr)), (not_notrec/len(not_recom_arr))]
recommen = [(rec_rec/len(recommend_arr)), (rec_prior/len(recommend_arr)), (rec_notrec/len(recommend_arr))]
veryrecom = [(ver_rec/len(very_recom_arr)), (ver_prior/len(very_recom_arr)), (ver_notrec/len(very_recom_arr))]
priorit = [(pri_rec/len(priority_arr)), (pri_prior/len(priority_arr)), (pri_notrec/len(priority_arr))]
specprior = [(spe_rec/len(spec_prior_arr)), (spe_prior/len(spec_prior_arr)), (spe_notrec/len(spec_prior_arr))]
# pandas
health_data = pd.DataFrame(data=np.array([not_recommend, recommen, veryrecom, priorit, specprior]).T,
                           columns=['Not_Recom', 'Recommend', 'Very_Recom', 'Priority', 'Spec_Prior'],
                           index=['recommended', 'priority', 'not_recom'])


if (freq == "parents"):
	print(tab1.draw())
	print("                              LIKELIHOOD TABLE ")
	print(parents_data)
if (freq == "has_nurs"):
	print(tab2.draw())
	print("                              LIKELIHOOD TABLE ")
	print(hasnurs_data)
if (freq == "form"):
	print(tab3.draw())
	print("                              LIKELIHOOD TABLE ")
	print(form_data)
if (freq == "children"):
	print(tab4.draw())
	print("                              LIKELIHOOD TABLE ")
	print(children_data)
if (freq == "housing"):
	print(tab5.draw())
	print("                              LIKELIHOOD TABLE ")
	print(housing_data)
if (freq == "finance"):
	print(tab6.draw())
	print("                              LIKELIHOOD TABLE ")
	print(finance_data)
if (freq == "social"):
	print(tab7.draw())
	print("                              LIKELIHOOD TABLE ")
	print(social_data)
if(freq == "health"):
	print(tab8.draw())
	print("                              LIKELIHOOD TABLE ")
	print(health_data)