#!/usr/bin/python
#-*- coding:utf-8 -*- 

import os
import sys
import time

branch_cfg = {
	"k" : r"E:\AuxLuaScripts\common\autocode",
	"tw" : r"D:\AuxLuaScripts\common\autocode",
	"t" : r"F:\AuxLuaScripts\common\autocode"
}

def main():
	branch = raw_input(u"Enter upload branch:")
	serverid = raw_input(u"Enter upload serverid:")

	port = int(serverid) - 100 + 32000
	autocode_path = branch_cfg[str(branch)]
	upload_origin = r"F:\workspace\project\trunk\client\Tools\putty/pscp.exe -batch -i F:\workspace\project\trunk\client\etc\bsn_gs_rsa.ppk -P "
	upload_cmd = upload_origin + str(port) + " -r " + str(autocode_path) + " root@192.168.1.210:/root/server/script/common"

	f = os.popen(upload_cmd,"r")
	d = f.read()
	print(d)
	f.close()

	f_name = "hot_update_" + str(int(time.time())) + ".lua"
	f_write_obj = open(f_name, "w")
	f_write_obj.writelines("ignores = {}\n")
	f_write_obj.writelines("lst = {\n")

	for root,dirs,files in os.walk(autocode_path,True):
		#print(dirs)
		for name in files:
			hot_update_file = str(os.path.join(root,name)).replace(str(autocode_path),"common/autocode")
			f_write_obj.writelines("    '" + hot_update_file.replace("\\","/") + "',")
			f_write_obj.writelines("\n")
	f_write_obj.writelines("}")
	f_write_obj.close()

	upload_hotupdate_file = upload_origin + str(port) + " " + str(os.path.abspath(f_name)) + " root@192.168.1.210:/root/server/script/hot_update"
	#print(upload_hotupdate_file)
	f = os.popen(upload_hotupdate_file,"r")
	d = f.read()
	print(d)
	f.close()

main()