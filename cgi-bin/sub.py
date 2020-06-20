import cgi
import html
import ipaddress

supnet_pc = ipaddress.ip_network('10.30.0.0/15')
supnet_voip = ipaddress.ip_network('10.32.0.0/15')

subnets_pc = list(supnet_pc.subnets(new_prefix=25))
subnets_voip = list(supnet_voip.subnets(new_prefix=25))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="../style.css">
            <title>BO subnet calc</title>
        </head>
        <body>
            <h1>-> Branch Office subnet calculator <-</h1>
            Office number:
            <form>
                <form action="/cgi-bin/bo_sub.py">
                <input type="text" name="OFFICE_NUM">
                <input type="submit">
            </form>
        """)

form = cgi.FieldStorage()
office_num = form.getfirst("OFFICE_NUM")
office_num = int(html.escape(office_num))

print("<hr>")
print("<h2>For office number: " + str(office_num) + "</h2>")

if int(office_num) >= len(subnets_pc):
    print('<h2 style="color:Tomato;">Out of range!</h2>')
    print('<h2 style="color:Tomato;">Maximum office number is ' + str(len(subnets_pc)-1) + '</h2>')
else:
    print("""<table style="width:40%">
                <tr>
                    <th>
                    </th>
                    <th>
                        PC
                    </ht>
                    <th>
                        Voip
                    </th>
                </tr>
                <tr>
                    <td>
                        <b>
                            Network
                        </b>
                    </td>
                    <td>
                    """)
    print(subnets_pc[office_num])
    print("""</td>
                    <td>""")
    print(subnets_voip[office_num])
    print("""
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>
                            Gateway
                        </b>
                    </td>
                    <td>""")
    print(list(subnets_pc[office_num].hosts())[0])
    print("""
                    </td>
                    <td>""")
    print(list(subnets_voip[office_num].hosts())[0])
    print("""
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>
                            Netmask
                        </b>
                    </td>
                    <td>""")
    print(subnets_pc[office_num].netmask)
    print("""
                    </td>
                    <td>""")
    print(subnets_voip[office_num].netmask)
    print("""
                    </td>
                </tr>
            </table>
        </body>
    """)
    print('</body>')