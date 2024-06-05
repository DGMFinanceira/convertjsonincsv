import pandas as pd
import json

# Seu JSON com múltiplos registros
data = '''
[
    {"CPStatus":"Indivíduo fez opt-in do Cadastro Positivo","Segment":"CPF contém somente negativações resolvidas","HasOnlyMinimumPII":false,"HasNegativeData":false,"HasInquiryData":true,"BestInfo":{"CPF":"01366401093","CPFStatus":"Regular","PersonName":{"Name":{"Full":"IASSUMARA DE MOURA RODRIGUES"}},"MotherName":{"Full":"IZAMAR DE MOURA RODRIGUES"},"DOB":{"Year":"1989","Month":"05","Day":"17"},"Age":"34","Gender":"N","Address":{"Street":"R SD LINO","Number":"180","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2023","Month":"04","Day":"20"}},"Email":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSUUUU@GMAIL.COM"},"PhoneNumber":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"28"},"PhoneNumber":"51997343583"},"MobilePhoneNumber":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"51993061178"},"PersonNameHistory":{"Name":[{"Name":{"Full":"IASSUMARA DE MOURA RODRIGUES"}},{"Name":{"Full":"IASSUMARA DE MOURA NULL RODRIGUES"}}]},"AddressHistory":{"Address":[{"Street":"R SD LINO","Number":"180","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2023","Month":"04","Day":"20"}},{"Street":"RUA SOLDADO LINO","Number":"180","Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2021","Month":"09","Day":"28"}},{"Street":"AVENIDA MARIANA DE SOUZA GUERRA","Number":"76","Neighborhood":"JARDIM VILA CARRAO","City":"SAO PAULO","State":"SP","PostalCode":"08340-220","DateLastSeen":{"Year":"2016","Month":"12","Day":"22"}},{"Street":"AVENIDA SANTA RITA","Number":"1135","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2016","Month":"02","Day":"01"}},{"Street":"RUA SOLDADO LINO","Number":"20","Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2016","Month":"02","Day":"01"}},{"Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2022","Month":"06","Day":"21"}},{"Street":"RUA I","Number":"105","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2021","Month":"05","Day":"17"}}]},"EmailHistory":{"Email":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSUUUU@GMAIL.COM"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSU_@HOTMAIL.COM"}]},"PhoneNumberHistory":{"PhoneNumber":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"28"},"PhoneNumber":"51997343583"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"5134796360"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"5134796807"},{"DateLastSeen":{"Year":"2019","Month":"11","Day":"05"},"PhoneNumber":"51998343583"},{"DateLastSeen":{"Year":"2020","Month":"05","Day":"15"},"PhoneNumber":"5134722095"}]},"MobilePhoneNumberHistory":{"MobilePhoneNumber":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"51993061178"}]}},"QuodScore":{"Score":"757","Message":"Capacidade de pagamento equivalente a média da população brasileira.","CreditRisk":"MÉDIO","ProbabilityOfPayment":83},"Negative":{"PendenciesControlCred":0,"Apontamentos":[],"LawSuitApontamentos":[],"CcfApontamentos":[],"Protests":{"data_consulta":"2023-06-09"},"TotalProtests":0,"TotalValorProtests":0},"Inquiries":{"InquiryCountLast30Days":0,"InquiryCountLast31to60Days":0,"InquiryCountLast61to90Days":1,"InquiryCountMore90Days":3,"InquiryDetails":{"InquiryDetail":[{"DateInquiry":{"Year":"2023","Month":"03","Day":"28"},"InquiryCount":1,"Segment":"Outros"},{"DateInquiry":{"Year":"2023","Month":"01","Day":"05"},"InquiryCount":1,"Segment":"0"},{"DateInquiry":{"Year":"2022","Month":"10","Day":"27"},"InquiryCount":1,"Segment":"Instituições Financeiras"},{"DateInquiry":{"Year":"2022","Month":"01","Day":"09"},"InquiryCount":1,"Segment":"0"}]}},"Indicators":[{"Risk":{"type":"ALTO","text":"O consumidor paga 100% ou a maioria das suas contas em dia na média dos últimos 12 meses."},"VariableName":"PaymentCommitmentScore","Description":"Este indicador considera o histórico de comportamento do consumidor sobre o pagamento de suas contas. Quanto mais alto, mais pontual.","Value":"78","Error":"--"},{"Risk":{"type":"MÉDIO","text":"O consumidor pode apresentar algumas divergências sobre o comportamento esperado na utilização de produtos financeiros."},"VariableName":"ProfileScore","Description":"Neste indicador, analisamos principalmente os produtos financeiros contratados pelo consumidor, como empréstimos, cheque especial, consórcios e cartões de crédito, para mostrar sua saúde de relacionamento com o mercado.","Value":"60","Error":"--"}],"EnterpriseData":{}},
    {"CPStatus":"Indivíduo fez opt-in do Cadastro Positivo","Segment":"CPF contém somente negativações resolvidas","HasOnlyMinimumPII":false,"HasNegativeData":false,"HasInquiryData":true,"BestInfo":{"CPF":"01366401093","CPFStatus":"Regular","PersonName":{"Name":{"Full":"IASSUMARA DE MOURA RODRIGUES"}},"MotherName":{"Full":"IZAMAR DE MOURA RODRIGUES"},"DOB":{"Year":"1989","Month":"05","Day":"17"},"Age":"34","Gender":"N","Address":{"Street":"R SD LINO","Number":"180","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2023","Month":"04","Day":"20"}},"Email":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSUUUU@GMAIL.COM"},"PhoneNumber":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"28"},"PhoneNumber":"51997343583"},"MobilePhoneNumber":{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"51993061178"},"PersonNameHistory":{"Name":[{"Name":{"Full":"IASSUMARA DE MOURA RODRIGUES"}},{"Name":{"Full":"IASSUMARA DE MOURA NULL RODRIGUES"}}]},"AddressHistory":{"Address":[{"Street":"R SD LINO","Number":"180","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2023","Month":"04","Day":"20"}},{"Street":"RUA SOLDADO LINO","Number":"180","Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2021","Month":"09","Day":"28"}},{"Street":"AVENIDA MARIANA DE SOUZA GUERRA","Number":"76","Neighborhood":"JARDIM VILA CARRAO","City":"SAO PAULO","State":"SP","PostalCode":"08340-220","DateLastSeen":{"Year":"2016","Month":"12","Day":"22"}},{"Street":"AVENIDA SANTA RITA","Number":"1135","Neighborhood":"CENTRO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2016","Month":"02","Day":"01"}},{"Street":"RUA SOLDADO LINO","Number":"20","Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2016","Month":"02","Day":"01"}},{"Neighborhood":"BERTO CIRIO","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2022","Month":"06","Day":"21"}},{"Street":"RUA I","Number":"105","City":"NOVA SANTA RITA","State":"RS","PostalCode":"92480-000","DateLastSeen":{"Year":"2021","Month":"05","Day":"17"}}]},"EmailHistory":{"Email":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSUUUU@GMAIL.COM"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"Email":"IASSU_@HOTMAIL.COM"}]},"PhoneNumberHistory":{"PhoneNumber":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"28"},"PhoneNumber":"51997343583"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"5134796360"},{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"5134796807"},{"DateLastSeen":{"Year":"2019","Month":"11","Day":"05"},"PhoneNumber":"51998343583"},{"DateLastSeen":{"Year":"2020","Month":"05","Day":"15"},"PhoneNumber":"5134722095"}]},"MobilePhoneNumberHistory":{"MobilePhoneNumber":[{"DateLastSeen":{"Year":"2023","Month":"04","Day":"30"},"PhoneNumber":"51993061178"}]}},"QuodScore":{"Score":"757","Message":"Capacidade de pagamento equivalente a média da população brasileira.","CreditRisk":"MÉDIO","ProbabilityOfPayment":83},"Negative":{"PendenciesControlCred":0,"Apontamentos":[],"LawSuitApontamentos":[],"CcfApontamentos":[],"Protests":{"data_consulta":"2023-06-09"},"TotalProtests":0,"TotalValorProtests":0},"Inquiries":{"InquiryCountLast30Days":0,"InquiryCountLast31to60Days":0,"InquiryCountLast61to90Days":1,"InquiryCountMore90Days":3,"InquiryDetails":{"InquiryDetail":[{"DateInquiry":{"Year":"2023","Month":"03","Day":"28"},"InquiryCount":1,"Segment":"Outros"},{"DateInquiry":{"Year":"2023","Month":"01","Day":"05"},"InquiryCount":1,"Segment":"0"},{"DateInquiry":{"Year":"2022","Month":"10","Day":"27"},"InquiryCount":1,"Segment":"Instituições Financeiras"},{"DateInquiry":{"Year":"2022","Month":"01","Day":"09"},"InquiryCount":1,"Segment":"0"}]}},"Indicators":[{"Risk":{"type":"ALTO","text":"O consumidor paga 100% ou a maioria das suas contas em dia na média dos últimos 12 meses."},"VariableName":"PaymentCommitmentScore","Description":"Este indicador considera o histórico de comportamento do consumidor sobre o pagamento de suas contas. Quanto mais alto, mais pontual.","Value":"78","Error":"--"},{"Risk":{"type":"MÉDIO","text":"O consumidor pode apresentar algumas divergências sobre o comportamento esperado na utilização de produtos financeiros."},"VariableName":"ProfileScore","Description":"Neste indicador, analisamos principalmente os produtos financeiros contratados pelo consumidor, como empréstimos, cheque especial, consórcios e cartões de crédito, para mostrar sua saúde de relacionamento com o mercado.","Value":"60","Error":"--"}],"EnterpriseData":{}}
]
'''

# Carregar o JSON
json_data = json.loads(data)

# Lista para armazenar DataFrames
df_list = []

# Iterar sobre cada registro JSON
for record in json_data:
    # Normalizar os dados principais
    df_main = pd.json_normalize(record, sep='_')

    # Normalizar os dados de Indicators
    df_indicators = pd.json_normalize(record['Indicators'], sep='_')
    for i, row in df_indicators.iterrows():
        for col in df_indicators.columns:
            df_main[f'Indicators_{i+1}_{col}'] = row[col]

    # Normalizar os dados de BestInfo_PersonNameHistory_Name
    df_person_name_history = pd.json_normalize(record['BestInfo']['PersonNameHistory']['Name'], sep='_')
    for i, row in df_person_name_history.iterrows():
        for col in df_person_name_history.columns:
            df_main[f'BestInfo_PersonNameHistory_Name_{i+1}_{col}'] = row[col]

    # Normalizar os dados de BestInfo_AddressHistory_Address
    df_address_history = pd.json_normalize(record['BestInfo']['AddressHistory']['Address'], sep='_')
    for i, row in df_address_history.iterrows():
        for col in df_address_history.columns:
            df_main[f'BestInfo_AddressHistory_Address_{i+1}_{col}'] = row[col]

    # Normalizar os dados de BestInfo_EmailHistory_Email
    df_email_history = pd.json_normalize(record['BestInfo']['EmailHistory']['Email'], sep='_')
    for i, row in df_email_history.iterrows():
        for col in df_email_history.columns:
            df_main[f'BestInfo_EmailHistory_Email_{i+1}_{col}'] = row[col]

    # Normalizar os dados de BestInfo_PhoneNumberHistory_PhoneNumber
    df_phone_number_history = pd.json_normalize(record['BestInfo']['PhoneNumberHistory']['PhoneNumber'], sep='_')
    for i, row in df_phone_number_history.iterrows():
        for col in df_phone_number_history.columns:
            df_main[f'BestInfo_PhoneNumberHistory_PhoneNumber_{i+1}_{col}'] = row[col]

    # Normalizar os dados de BestInfo_MobilePhoneNumberHistory_MobilePhoneNumber
    df_mobile_phone_number_history = pd.json_normalize(record['BestInfo']['MobilePhoneNumberHistory']['MobilePhoneNumber'], sep='_')
    for i, row in df_mobile_phone_number_history.iterrows():
        for col in df_mobile_phone_number_history.columns:
            df_main[f'BestInfo_MobilePhoneNumberHistory_MobilePhoneNumber_{i+1}_{col}'] = row[col]

    # Normalizar os dados de Inquiries_InquiryDetails_InquiryDetail
    df_inquiry_details = pd.json_normalize(record['Inquiries']['InquiryDetails']['InquiryDetail'], sep='_')
    for i, row in df_inquiry_details.iterrows():
        for col in df_inquiry_details.columns:
            df_main[f'Inquiries_InquiryDetails_InquiryDetail_{i+1}_{col}'] = row[col]

    # Adicionar o DataFrame à lista
    df_list.append(df_main)

# Concatenar todos os DataFrames na lista
df_final = pd.concat(df_list, ignore_index=True)

# Excluir as colunas especificadas
columns_to_drop = [
    'Indicators', 
    'BestInfo_PersonNameHistory_Name', 
    'BestInfo_AddressHistory_Address', 
    'BestInfo_EmailHistory_Email', 
    'BestInfo_PhoneNumberHistory_PhoneNumber', 
    'BestInfo_MobilePhoneNumberHistory_MobilePhoneNumber', 
    'Inquiries_InquiryDetails_InquiryDetail'
]

df_final.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Exportar para Excel
df_final.to_excel('planilhaOriginal.xlsx', index=False)