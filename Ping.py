import os
import threading
import http.server
import socketserver

port = 8080
address = ("", port)
server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
httpd = server(address, handler)



class Server():
    state_ping = 0
    site = "000"
    hostname = ""

    def __init__(self, site):
        self.site = site
        self.ping_server()
        self.hostname = "snt.mag" + self.site
        self.T = threading.Thread(target=self.ping_server)
        self.T.start()
        # self.ping_server()

    def ping_server(self):
        response = os.system("ping -c 1 -n 1 " + self.hostname + ">NUL 2>&1")
        if response == 0:
            self.state_ping = 1
        else:
            self.state_ping = 0

    def ping_status_sync(self):
        return self.state_ping

    def ping_status(self):
        self.T.join()
        return self.state_ping


def serverlist():
    server_list = ['003', '004', '005', '006', '007', '009', '010', '011', '012', '013', '014', '015', '016', '018',
                   '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '032', '035',
                   '036', '037', '039', '040', '041', '043', '044', '045', '046', '047', '048', '049', '050', '051',
                   '052', '053', '054', '055', '056', '059', '060', '061', '062', '063', '064', '066', '067', '069',
                   '071', '072', '073', '074', '075', '076', '077', '078', '080', '081', '082', '084', '085', '088',
                   '089', '100', '110', '111', '112', '114', '115', '116', '117', '119', '130', '131', '132', '133',
                   '135', '137', '138', '139', '140', '142', '143', '144', '145', '146', '147', '148', '150', '151',
                   '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165',
                   '166', '167', '168', '168', '169', '171', '172', '173', '174', '175', '176', '177', '178', '179',
                   '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193',
                   '194', '195', '196', '198', '199', '205', '206', '292', '293', '294', '295', '296', '297', '298',
                   '300', '380']

    server_dict = {}
    for i in server_list:
        # print("Chargement du serveur: ", i)
        server_dict[i] = Server(i)
    return server_dict


mydict = serverlist()

# print(mydict["166"].state_ping)
print(mydict["380"].ping_status())
print(mydict["166"].ping_status())

print("Serveur Web démarré sur le port : ", port)
httpd.serve_forever()

# mag003 = Serveur(site=str("003"))
# mag006 = Serveur(site=str("006"),state_ping=0)

# mag006 = Serveur(site=006)


# print("Le site :", mag003.site, "est en state :", mag003.state_ping)
# print("Le site :", mag006.site, "est en state :", mag006.state_ping)


# if isinstance(mag003, Serveur):
#    print("Mag : 003 est bien une instance de la classe Serveur !")
# else:
#    print("Mag : 003 n'est pas une instance de la classe Serveur !")
