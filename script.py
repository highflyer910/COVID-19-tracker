from covid import Covid
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

covid=Covid()
def status():
    def search():
        cname=ctname.get()
        if cname=='':
            return messagebox.showerror('Error','Enter country name')
        else:
            data=covid.get_status_by_country_name(cname)
            sta=Toplevel()
            sta.geometry('200x300')
            sta.configure(bg="#1a1a1a")
            sta.title(cname)
            Label(sta,text='   ').grid(column=1)
            Label(sta,text='COUNTRY STATUS',font='Roboto 12 bold',bg="#1a1a1a", fg="white").grid(row=1,column=2)
            Label(sta,text='Total confirmed cases: '+str(data['confirmed']), fg="cyan",bg="#1a1a1a").grid(row=2,column=2)
            Label(sta,text='Total active cases: '+str(data['active']), fg="violet",bg="#1a1a1a").grid(row=3,column=2)
            Label(sta,text='Total recoveries: '+str(data['recovered']), fg="light green",bg="#1a1a1a").grid(row=4,column=2)
            Label(sta,text='Total deaths: '+str(data['deaths']), fg="orangered",bg="#1a1a1a").grid(row=5,column=2)
            st.destroy()
    ctname=StringVar()
    st=Toplevel()
    st.geometry('300x100')
    st.configure(bg='#1a1a1a')
    st.title('Status')
    Label(st,text='Country status',font='Roboto 12 bold',bg='#1a1a1a',fg="white").grid(column=1)
    Label(st,text='Enter the country name:',bg='#1a1a1a',fg="white").grid(row=2)
    Entry(st,width=17,textvariable=ctname, bg="light yellow").grid(row=2,column=1)
    Button(st,text='Search',bg='#1a1a1a',fg="white",command=search).grid(row=2,column=2)


window=Tk()
window.geometry('200x300')
window.configure(bg='#1a1a1a')
window.title('Covid-19 Update')
Label(window,text='  ').grid(column=1)
Label(window,text='COVID-19 Update',font='Roboto 12 bold', bg='#1a1a1a',fg="white").grid(row=1, column=2)
Label(window,text='Total confirmed cases: '+str(covid.get_total_confirmed_cases()), fg="cyan",bg='#1a1a1a').grid(row=2,column=2)
Label(window,text='Total active cases: '+str(covid.get_total_active_cases()), fg="violet",bg='#1a1a1a').grid(row=3,column=2)
Label(window,text='Total recoveries: '+str(covid.get_total_recovered()), fg="light green",bg='#1a1a1a').grid(row=4,column=2)
Label(window,text='Total deaths: '+str(covid.get_total_deaths()), fg="orangered",bg='#1a1a1a').grid(row=5,column=2)
Button(window,text='Get the COVID-19 data',bg='#1a1a1a', fg="white",command=status).grid(row=6,column=2)


window.mainloop()