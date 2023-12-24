from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import openpyxl
import numpy as np

navegador = webdriver.Firefox()

navegador.get("https://app.docusign.com/documents?view=powerforms")

navegador.get("https://www.autocompara.com.br/cotacao/sobre-voce")

try:
    navegador.find_element('xpath',"/html/body/ac-cookie-consent/div[2]/ac-button/button").click() 
except:
    time.sleep(0.01)

lista = pd.read_excel(r"autocompara.xlsx")

valor = len(lista.axes[0])

x = 0

while x != valor:
    try:

        time.sleep(2)
        WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[1]/mat-form-field/div/div[1]/div[4]/input")))

        y = 0

        df = pd.DataFrame()

        #Nome
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[1]/mat-form-field/div/div[1]/div[4]/input").clear()
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[1]/mat-form-field/div/div[1]/div[4]/input").send_keys('Anderson Maltine')

        time.sleep(1)
        
        #CPF
        a = str(lista.iloc[x,y])
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/div[1]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").clear()
        time.sleep(0.5)
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/div[1]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").send_keys(a)
        y = y + 1 

        time.sleep(1)

        #Data Nascimento
        b = lista.iloc[x,y]
        b = b.strftime('%d/%m/%Y')
        b = b.replace("/","")
        b = str(b)
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-datepicker/mat-form-field/div/div[1]/div[4]/input").clear()
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-datepicker/mat-form-field/div/div[1]/div[4]/input").send_keys(b)
        y = y + 1

        time.sleep(1)

        #Email
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[2]/mat-form-field/div/div[1]/div[4]/input").clear()
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[2]/mat-form-field/div/div[1]/div[4]/input").send_keys('andersonmaltine@hotmail.com')

        time.sleep(1)

        #Celular
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[3]/mat-form-field/div/div[1]/div[4]/input").clear()
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/ac-input-text[3]/mat-form-field/div/div[1]/div[4]/input").send_keys('11941258810')

        time.sleep(1)
        
        elemQueVcQuer = navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/div[5]/ac-checkbox/div/input")
                        
        if elemQueVcQuer.is_selected():
            pass 
        else:
            navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[1]/div[5]/ac-checkbox/div/input").click() 


        time.sleep(1)

        navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/user-form/content-layout/div/div[2]/div/form/div[2]/ac-button/button").click()

        WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[1]/span[2]/ac-button[2]/button")))
        time.sleep(5)

        #Seguro auto ou moto
        c = str(lista.iloc[x,y])
        if c == '2':
            navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[1]/span[2]/ac-button[2]/button").click()
        else:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)
        WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[1]/ac-toggle/div/div[2]")))

        #ZeroKM
        d = str(lista.iloc[x,y])
        if d == '1':
            navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[1]/ac-toggle/div/div[2]/p").click()
        else:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1) 

        #Placa
        e = str(lista.iloc[x,y])
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[3]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").send_keys(e)
        y = y + 1

        msg = ''
        try:
            time.sleep(2)
            msg = navegador.find_element(By.XPATH,'/html/body/app-root/component-modal/section/div/confirmation-modal/div/h2').text
            if msg == 'Placa não encontrada.':
                navegador.find_element('xpath',"/html/body/app-root/component-modal/section/div/confirmation-modal/div/div/ac-button/button").click()
                time.sleep(2) 
            elif msg == 'Você informou uma placa de Moto.':
                navegador.find_element('xpath',"/html/body/app-root/component-modal/section/div/confirmation-modal/div/div/ac-button[2]/button").click()
                time.sleep(2) 
            else:
                pass
        except:
            pass

        WebDriverWait(navegador, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[1]/ac-toggle/div/div[2]")))
        time.sleep(2)

        try: 
            #Ano/Modelo
            f = str(lista.iloc[x,y]) 
            if msg == 'Placa não encontrada.':
                navegador.find_element(By.XPATH,"/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[3]/ac-input-select/mat-form-field/div/div[1]/div[4]/mat-select").click()
                time.sleep(1)
                idselectano = 1
                while idselectano < 100:
                    idselectano = str(idselectano)
                    diretorioselectver = "/html/body/div[" + idselectano + "]/div[2]/div/div/div/mat-option[1]"
                    try:
                        navegador.find_element(By.XPATH,diretorioselectver).click()
                        idselectano = 101
                    except:
                        idselectano = int(idselectano)
                        idselectano = idselectano + 1
                time.sleep(2)
            else:
                pass
        except:
            pass
        time.sleep(1)
        y= y + 1

        time.sleep(1)
        print(msg)
        try: 
            #Marca/Modelo
            g = str(lista.iloc[x,y]) 
            if msg == 'Placa não encontrada.':
                navegador.find_element(By.XPATH,"/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[4]/ac-autocomplete/mat-form-field/div/div[1]/div[4]/input").send_keys(g)
                action = ActionChains(navegador)
                action.send_keys(Keys.ARROW_DOWN)
                action.send_keys(Keys.ENTER)
                action.perform()
            else:
                pass
        except:
            pass
        pass
        y= y + 1

        try: 
            #Versao
            h = str(lista.iloc[x,y]) 
            navegador.find_element(By.XPATH,"/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[4]/ac-input-select/mat-form-field/div/div[1]/div[4]/mat-select").click()
            time.sleep(1)
            idselect = 1
            while idselect < 100:
                idselect = str(idselect)
                diretorioselectver = "/html/body/div[" + idselect + "]/div[2]/div/div/div/mat-option[1]"
                try:
                    navegador.find_element(By.XPATH,diretorioselectver).click()
                    idselect = 101
                except:
                    idselect = int(idselect)
                    idselect = idselect + 1 
        except:
            pass
        y = y + 1


        try:
            #Blindagem
            i = str(lista.iloc[x,y])
            if i == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[1]/ac-toggle/div/div[2]').click()
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(3)

        try:
            #Data Blindagem
            j = lista.iloc[x,y]
            j = j.strftime('%d/%m/%Y')
            j = j.replace("/","")
            j = str(j)
            if i == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[1]/ac-datepicker/mat-form-field/div/div[1]/div[4]/input').send_keys(j)
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Valor Blindagem
            k = str(lista.iloc[x,y])
            if i == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[1]/ac-input-currency/mat-form-field/div/div[1]/div[4]/input').send_keys(k)
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Kit Gás
            l = str(lista.iloc[x,y])
            if l == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[2]/ac-toggle/div/div[2]').click()
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Data Kit Gas
            m = lista.iloc[x,y]
            m = m.strftime('%d/%m/%Y')
            m = m.replace("/","")
            m = str(m)
            if l == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[2]/ac-datepicker/mat-form-field/div/div[1]/div[4]/input').send_keys(m)
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Valor Kit Gas
            n = str(lista.iloc[x,y])
            if l == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[2]/ac-input-currency/mat-form-field/div/div[1]/div[4]/input').send_keys(n)
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Beneficio Fiscal
            o = str(lista.iloc[x,y])
            if o == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/div/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/ac-checkbox[1]/div/input').click()
            elif o == '2':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/div/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/ac-checkbox[2]/div/input').click()
            elif o == '3':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/div/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/ac-checkbox[1]/div/input').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[5]/div[3]/ac-checkbox[2]/div/input').click()
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(2)
        try:
            navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/vehicle-form/content-layout/div/div[2]/div/form/div[6]/ac-button/button').click() #Clicar em proximo
        except:
            time.sleep(0.01)
            
        WebDriverWait(navegador, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[2]/ac-input-text/mat-form-field/div/div[1]/div[4]/input")))

        time.sleep(1)

        #CEP Pernoite
        p = str(lista.iloc[x,y])

        if len(p) == 8:
            p = p
        elif len(p) == 7:
            p = '0' + p
        elif len(p) == 6:
            p = '00' + p
        else:
            p = '000' + p
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[2]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").clear()
        navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[2]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").send_keys(p)
        time.sleep(2)
        cepmsg = navegador.find_element(By.XPATH,'/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[3]/p').text
        if cepmsg == 'Cep inválido':
            navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[2]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").clear()
            navegador.find_element(By.XPATH, "/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[1]/div[2]/ac-input-text/mat-form-field/div/div[1]/div[4]/input").send_keys('02112002')
        else:
            pass
        y = y + 1

        time.sleep(1)

        try:
            #Condutor menor do que 25 anos
            q = str(lista.iloc[x,y])
            if q == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[2]/ac-toggle/div/div[2]').click()
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Atividade Comercial
            r = str(lista.iloc[x,y])
            if r == '1':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[3]/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[4]/div/div/ac-radio[1]/div/input').click()
            elif r == '2':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[3]/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[4]/div/div/ac-radio[2]/div/input').click()
            elif r == '3':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[3]/ac-toggle/div/div[2]').click()
                time.sleep(1)
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[4]/div/div/ac-radio[3]/div/input').click()
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        try:
            #Tipo Renovação
            s = str(lista.iloc[x,y])
            if s == '2':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/ac-toggle/div/div[2]').click()
            else:
                valoridtprenov = navegador.find_element(By.XPATH,'/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/ac-toggle/div/div[2]/p').get_attribute('data-testid')
                if valoridtprenov == 'yes':
                    navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/ac-toggle/div/div[2]').click()
                else:
                    pass
        except: 
            time.sleep(0.1)
        y = y + 1

        time.sleep(1)

        #Classe Bônus
        t = str(lista.iloc[x,y]) 
        if s == '2':
            WebDriverWait(navegador, 40).until(EC.presence_of_element_located((By.XPATH, "html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/div/div[1]/div/ac-input-select/mat-form-field/div/div[1]/div[4]/mat-select")))
            navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/div/div[1]/div/ac-input-select/mat-form-field/div/div[1]/div[4]/mat-select').click()
            time.sleep(1)
            div = 17
            t = int(t)
            t = t + 1
            while div <= 23:
                div = str(div)
                t = str(t)
                diret = "/html/body/div[" + div + "]/div[2]/div/div/div/mat-option[" + t + "]"  
                div = int(div)
                try:
                    navegador.find_element('xpath',diret).click()
                    div = 24
                except:
                    div = div + 1
        else:
            time.sleep(0.01)
        y = y + 1

        try:
            #Data de Vencimento Seguro
            u = lista.iloc[x,y]
            u = u.strftime('%d/%m/%Y')
            u = u.replace("/","")
            u = str(u)
            if s == '2':
                navegador.find_element(By.XPATH, '/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[5]/div/div/div[2]/div/ac-datepicker/mat-form-field/div/div[1]/div[4]/input').send_keys(u)
            else:
                time.sleep(0.01)
        except:
            time.sleep(0.1)
        y = y + 1

        navegador.find_element('xpath',"/html/body/app-root/app-quotation-form/div/div[2]/location-form/content-layout/div/div[2]/div/form/div[8]/ac-button/button").click()

        time.sleep(10)

        WebDriverWait(navegador, 500).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card/div/div[2]/div[1]/figure/div/img")))

        idcong = 1

        while idcong < 100:
            idcong = str(idcong) 
            cong = ''
            vl = ''
            fr = ''
            
            try:
                pers = navegador.find_element(By.XPATH,'/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ul/li[1]').text 
                pers = pers.replace(" ", "")
            except:
                pers = ''

            print(pers)

            if pers != '':
                if idcong == '1':
                    congxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/figure/div/img'
                    vlxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/div/h3'
                    frxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/div/p'
                else:
                    congxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card[' + idcong + ']/div/div/div[1]/figure/div/img'
                    vlxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card['+ idcong + ']/div/div/div[1]/div/h3'
                    frxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[1]/div/offer-card/div/ac-simple-card['+ idcong + ']/div/div/div[1]/div/p'
            else:
                if idcong == '1':
                    congxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/figure/div/img'
                    vlxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/div/h3'
                    frxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card[1]/div/div[2]/div[1]/div/p'
                else:
                    congxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card[' + idcong + ']/div/div/div[1]/figure/div/img'
                    vlxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card['+ idcong + ']/div/div/div[1]/div/h3'
                    frxpath = '/html/body/app-root/ac-offers/div/div/div[1]/div[1]/ac-tabs/ac-tab[2]/div/offer-card/div/ac-simple-card['+ idcong + ']/div/div/div[1]/div/p'

            idcong = int(idcong) 

            try:
                cong = navegador.find_element(By.XPATH,congxpath).get_attribute('title')
                cong = cong.replace("Logo","")
                vl = navegador.find_element(By.XPATH,vlxpath).text
                fr = navegador.find_element(By.XPATH,frxpath).text
                dict_cong = {"Index": x, "Congenere" : cong, "Valor Premio": vl, "Valor Franquia": fr, "Cobertura" : pers}
                df = pd.DataFrame([dict_cong])
                df.to_csv(r"\\hdist02\departamentos\ProdutoAuto\Analytics_Digital\Victor Yoshida\Premio_Congenere.csv", index=False,sep=';',encoding='utf-8-sig',mode='a',header = None)
                idcong = idcong + 1
            except:
                idcong = 101

        print(df)

        x = str(x)

        time.sleep(3)

        navegador.find_element('xpath',"/html/body/app-root/ac-offers/div/div/div[1]/div[1]/div/ac-link").click()

        time.sleep(2)

        navegador.find_element('xpath',"/html/body/app-root/ac-offers/ac-modal[7]/div/div/confirmation-modal/div/div/ac-button[2]/button").click()

        x = int(x)

        x = x + 1

    except:
        navegador.get("https://www.autocompara.com.br/cotacao/sobre-voce")

        try:
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ac-offers/div/div/div[1]/div[1]/div/ac-link")))

            navegador.find_element('xpath',"/html/body/app-root/ac-offers/div/div/div[1]/div[1]/div/ac-link").click()

            time.sleep(2)

            navegador.find_element('xpath',"/html/body/app-root/ac-offers/ac-modal[7]/div/div/confirmation-modal/div/div/ac-button[2]/button").click()
        except:
            time.sleep(0.01)


