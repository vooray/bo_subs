import cgi
import html
import ipaddress

sub_pc = ipaddress.ip_network('10.30.0.0/15')
sub_voip = ipaddress.ip_network('10.32.0.0/15')

sub_pc_subnets = list(sub_pc.subnets(new_prefix=25))
sub_voip_subnets = list(sub_voip.subnets(new_prefix=25))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="../style.css">
            <title>BO subnet calc</title>
        </head>
        <body>
            <h1>/// BO subnet calc</h1>
            Office num:
            <form>
                <form action="/cgi-bin/bo_sub.py">
                <input type="text" name="BO_NUM">
                <input type="submit">
            </form>
        """)

form = cgi.FieldStorage()
bo_num = form.getfirst("BO_NUM")
bo_num = int(html.escape(bo_num))

print("<hr>")

print("<h2>For office number: " + str(bo_num) + "</h2>")

if int(bo_num) >= len(sub_pc_subnets):
    print('<h2 style="color:Tomato;">Out of range!</h2>')
    print('<h2 style="color:Tomato;">Maximum office num is ' + str(len(sub_pc_subnets)-1) + '</h2>')
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
    print(sub_pc_subnets[bo_num])
    print("""</td>
                    <td>""")
    print(sub_voip_subnets[bo_num])
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
    print(list(sub_pc_subnets[bo_num].hosts())[0])
    print("""
                    </td>
                    <td>""")
    print(list(sub_voip_subnets[bo_num].hosts())[0])
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
    print(sub_pc_subnets[bo_num].netmask)
    print("""
                    </td>
                    <td>""")
    print(sub_voip_subnets[bo_num].netmask)
    print("""
                    </td>
                </tr>
            </table>
        </body>
    """)