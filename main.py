import PySimpleGUI as sg
import layouts

def main():

    window = sg.Window('Title',layouts.layout_main)

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == '__main__':
    sg.theme('DarkGrey6')
    main()
