# layouts defs
import PySimpleGUI as sg

sg.theme('DarkGrey6')

layout_inputs = [[sg.Text('01:Neck',expand_x=True),sg.InputText(k='kneck',s=20)],
                     [sg.Text('02:Left Biceps',expand_x=True),sg.InputText(k='kleftbiceps',s=20)],
                     [sg.Text('03:Right Biceps',expand_x=True),sg.InputText(k='krightbiceps',s=20)],
                     [sg.Text('04:Left Forearm',expand_x=True),sg.InputText(k='kleftforearm',s=20)],
                     [sg.Text('05:Right Forearm',expand_x=True),sg.InputText(k='krightforearm',s=20)],
                     [sg.Text('06:Chest',expand_x=True),sg.InputText(k='kchest',s=20)],
                     [sg.Text('07:Waist',expand_x=True),sg.InputText(k='kwaist',s=20)],
                     [sg.Text('08:Hips',expand_x=True),sg.InputText(k='khips',s=20)],
                     [sg.Text('09:Left Thigh',expand_x=True),sg.InputText(k='kleftthigh',s=20)],
                     [sg.Text('10:Right Thigh',expand_x=True),sg.InputText(k='krightthigh',s=20)],
                     [sg.Text('11:Left Calf',expand_x=True),sg.InputText(k='kleftcalf',s=20)],
                     [sg.Text('12:Right Calf',expand_x=True),sg.InputText(k='krightcalf',s=20)],
                     [sg.Text('13:Fat Ratio (caliper)',expand_x=True),sg.InputText(k='kfatratio',s=20)],
                    ]

layout_schema = [[sg.Image(source='silhouette.png',s=(200,200))]]

layout_main = [[sg.Column(layout_inputs),sg.VerticalSeparator(),sg.Column(layout_schema)],
             [sg.Button('Exit'),sg.Button('Push')],
             ]
