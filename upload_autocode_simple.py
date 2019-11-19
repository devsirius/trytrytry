#!/usr/bin/python
#-*- coding:utf-8 -*- 

import os
import sys

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
	upload_cmd = upload_origin + str(port) + " -r " + str(autocode_path) + " root@192.168.1.210:/root/server/script/common/autocode"

	f = os.popen(upload_cmd,"r")
	d = f.read()
	print(d)
	f.close()

main()