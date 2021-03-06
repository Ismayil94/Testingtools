'''
Created on Nov 6, 2019

@author: ismayil.aliyev
'''
import tkinter as tk
from xml.dom import minidom
from random import randint

import uuid
import time


timestr = time.strftime("%Y%m%d-%H%M%S")
#method for generating statement
def generatestatement():
    #variables
    firstname=str(e1.get())
    lastname=str(e2.get())
    fullname=firstname+" "+lastname
    REFNO=str(e3.get())
    IBAN=str(e4.get())
    AMOUNT=str(e5.get())
    IDENTITY=str(e6.get())
    DIRECTORY=str(e7.get())
    #unique random values
    id_unique=str(uuid.uuid4())
    AcctSvcrRef=str(uuid.uuid4())
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #unique_filename = timestr +"_"+str(uuid.uuid4())
    unique_filename = timestr+"_"+str(uuid.uuid4())+REFNO

    randomID = str(randint(1000000000000000000000, 9999999999999999999999))
    
    
    doc = minidom.Document()
    doc.toprettyxml(encoding="utf-8")
    #doc.setAttribute('encoding', 'UTF-8')
    
    root = doc.createElement('Document')
    root.setAttribute('xmlns', 'urn:iso:std:iso:20022:tech:xsd:camt.052.001.02')
    doc.appendChild(root)
    #BkToCstmrAcctRpt part
    underroot = doc.createElement('BkToCstmrAcctRpt')
    GrpHdr= doc.createElement('GrpHdr')
    underroot.appendChild(GrpHdr)
    root.appendChild(underroot)
    MsgId=doc.createElement('MsgId')
    GrpHdr.appendChild(MsgId)
    CreDtTm=doc.createElement('CreDtTm')
    GrpHdr.appendChild(CreDtTm)
    textMsgId = doc.createTextNode(randomID)
    MsgId.appendChild(textMsgId)
    textMsgId = doc.createTextNode('2019-10-14T13:01:07')
    CreDtTm.appendChild(textMsgId)
    #RPT block
    Rpt=doc.createElement('Rpt')
    underroot.appendChild(Rpt)
    
    Id=doc.createElement('Id')
    Rpt.appendChild(Id)
    IDId = doc.createTextNode(randomID)
    Id.appendChild(IDId)
    
    CreDtTm2=doc.createElement('CreDtTm')
    Rpt.appendChild(CreDtTm2)
    CreDtTm2text = doc.createTextNode('2019-09-20T16:00:46')
    CreDtTm2.appendChild(CreDtTm2text)
    
    #FrToDt part
    FrToDt=doc.createElement('FrToDt')
    Rpt.appendChild(FrToDt)
    FrDtTm=doc.createElement('FrDtTm')
    FrToDt.appendChild(FrDtTm)
    FrDtTmtext = doc.createTextNode('2019-10-14T00:00:00')
    FrDtTm.appendChild(FrDtTmtext)
    ToDtTm=doc.createElement('ToDtTm')
    FrToDt.appendChild(ToDtTm)
    ToDtTmtext = doc.createTextNode('2019-10-14T16:00:46')
    ToDtTm.appendChild(ToDtTmtext)
    #Acct part
    Acct=doc.createElement('Acct')
    Rpt.appendChild(Acct)
    Id_Acct=doc.createElement('Id')
    Acct.appendChild(Id_Acct)
    Iban=doc.createElement('IBAN')
    Id_Acct.appendChild(Iban)
    Ibantext = doc.createTextNode(IBAN)
    Iban.appendChild(Ibantext)
    Ccy=doc.createElement('Ccy')
    Acct.appendChild(Ccy)
    CcyText = doc.createTextNode('EUR')
    Ccy.appendChild(CcyText)
    #Ownr part
    Ownr=doc.createElement('Ownr')
    Acct.appendChild(Ownr)
    Nm=doc.createElement('Nm')
    Ownr.appendChild(Nm)
    
    #name and surname variable
    NmText = doc.createTextNode(fullname)
    Nm.appendChild(NmText)
    PstlAdr=doc.createElement('PstlAdr')
    Ownr.appendChild(PstlAdr)
    Ctry=doc.createElement('Ctry')
    PstlAdr.appendChild(Ctry)
    CtryText = doc.createTextNode('LT')
    Ctry.appendChild(CtryText)
    AdrLine=doc.createElement('AdrLine')
    PstlAdr.appendChild(AdrLine)
    AdrLineText = doc.createTextNode('KAREIVI?? 11B, Vilnius')
    AdrLine.appendChild(AdrLineText)
    IdOwnr=doc.createElement('Id')
    Ownr.appendChild(IdOwnr)
    OrgId=doc.createElement('OrgId')
    IdOwnr.appendChild(OrgId)
    Othr=doc.createElement('Othr')
    OrgId.appendChild(Othr)
    IdOthr=doc.createElement('Id')
    Othr.appendChild(IdOthr)
    IdOthrText = doc.createTextNode(IDENTITY)
    IdOthr.appendChild(IdOthrText)
    #Svcr part
    Svcr=doc.createElement('Svcr')
    Acct.appendChild(Svcr)
    FinInstnId=doc.createElement('FinInstnId')
    Svcr.appendChild(FinInstnId)
    BIC=doc.createElement('BIC')
    FinInstnId.appendChild(BIC)
    BICText = doc.createTextNode('HABALT22')
    BIC.appendChild(BICText)
    Nm=doc.createElement('Nm')
    FinInstnId.appendChild(Nm)
    NmText = doc.createTextNode('Swedbank AB')
    Nm.appendChild(NmText)
    PstlAdr=doc.createElement('PstlAdr')
    FinInstnId.appendChild(PstlAdr)
    Ctry=doc.createElement('Ctry')
    PstlAdr.appendChild(Ctry)
    CtryText = doc.createTextNode('LT')
    Ctry.appendChild(CtryText)
    AdrLine2=doc.createElement('AdrLine')
    PstlAdr.appendChild(AdrLine2)
    AdrLine2Text = doc.createTextNode('Konstitucijos pr. 20A, 03502 Vilnius')
    AdrLine2.appendChild(AdrLine2Text)
    Othr2=doc.createElement('Othr')
    FinInstnId.appendChild(Othr2)
    IdOthr2=doc.createElement('Id')
    Othr2.appendChild(IdOthr2)
    IdOthr2Text = doc.createTextNode(IDENTITY)
    IdOthr2.appendChild(IdOthr2Text)
    SchmeNm=doc.createElement('SchmeNm')
    Othr2.appendChild(SchmeNm)
    Cd=doc.createElement('Cd')
    SchmeNm.appendChild(Cd)
    CdText = doc.createTextNode('COID')
    Cd.appendChild(CdText)
    #Ntry part
    Ntry=doc.createElement('Ntry')
    Rpt.appendChild(Ntry)
    NtryRef=doc.createElement('NtryRef')
    Ntry.appendChild(NtryRef)
    NtryRefText = doc.createTextNode('2019091900000000-15')
    NtryRef.appendChild(NtryRefText)
    Amt=doc.createElement('Amt')
    Amt.setAttribute('Ccy', 'EUR')
    Ntry.appendChild(Amt)
    AmtText = doc.createTextNode('%s.00'%AMOUNT)
    Amt.appendChild(AmtText)
    CdtDbtInd=doc.createElement('CdtDbtInd')
    Ntry.appendChild(CdtDbtInd)
    CdtDbtIndText = doc.createTextNode('CRDT')
    CdtDbtInd.appendChild(CdtDbtIndText)
    Sts=doc.createElement('Sts')
    Ntry.appendChild(Sts)
    StsText = doc.createTextNode('BOOK')
    Sts.appendChild(StsText)
    BookgDt=doc.createElement('BookgDt')
    Ntry.appendChild(BookgDt)
    Dt=doc.createElement('Dt')
    BookgDt.appendChild(Dt)
    DtText = doc.createTextNode('2019-10-14')
    Dt.appendChild(DtText)
    ValDt=doc.createElement('ValDt')
    Ntry.appendChild(ValDt)
    Dt2=doc.createElement('Dt')
    ValDt.appendChild(Dt2)
    Dt2Text = doc.createTextNode('2019-10-14')
    Dt2.appendChild(Dt2Text)
    AcctSvcrRef=doc.createElement('AcctSvcrRef')
    Ntry.appendChild(AcctSvcrRef)
    AcctSvcrRefText = doc.createTextNode(randomID)
    AcctSvcrRef.appendChild(AcctSvcrRefText)
    BkTxCd=doc.createElement('BkTxCd')
    Ntry.appendChild(BkTxCd)
    Domn=doc.createElement('Domn')
    BkTxCd.appendChild(Domn)
    Cd=doc.createElement('Cd')
    Domn.appendChild(Cd)
    CdText = doc.createTextNode('PMNT')
    Cd.appendChild(CdText)
    Fmly=doc.createElement('Fmly')
    Domn.appendChild(Fmly)
    Cd2=doc.createElement('Cd')
    Fmly.appendChild(Cd2)
    Cd2Text = doc.createTextNode('RCDT')
    Cd2.appendChild(Cd2Text)
    SubFmlyCd=doc.createElement('SubFmlyCd')
    Fmly.appendChild(SubFmlyCd)
    SubFmlyCdText = doc.createTextNode('BOOK')
    SubFmlyCd.appendChild(SubFmlyCdText)
    Prtry=doc.createElement('Prtry')
    BkTxCd.appendChild(Prtry)
    Cd3=doc.createElement('Cd')
    Prtry.appendChild(Cd3)
    Cd3Text = doc.createTextNode('BL')
    Cd3.appendChild(Cd3Text)
    Issr=doc.createElement('Issr')
    Prtry.appendChild(Issr)
    IssrText = doc.createTextNode('Swedbank AB')
    Issr.appendChild(IssrText)
    #NtryDtls part
    NtryDtls=doc.createElement('NtryDtls')
    Ntry.appendChild(NtryDtls)
    TxDtls=doc.createElement('TxDtls')
    NtryDtls.appendChild(TxDtls)
    Refs=doc.createElement('Refs')
    TxDtls.appendChild(Refs)
    AcctSvcrRef_Refs=doc.createElement('AcctSvcrRef')
    Refs.appendChild(AcctSvcrRef_Refs)
    AcctSvcrRef_RefsText = doc.createTextNode('2019091900000000-15')
    AcctSvcrRef_Refs.appendChild(AcctSvcrRef_RefsText)
    InstrId=doc.createElement('InstrId')
    Refs.appendChild(InstrId)
    InstrIdText = doc.createTextNode('56')
    InstrId.appendChild(InstrIdText)
    AmtDtls=doc.createElement('AmtDtls')
    TxDtls.appendChild(AmtDtls)
    InstdAmt=doc.createElement('InstdAmt')
    AmtDtls.appendChild(InstdAmt)
    AmtInstdAmt=doc.createElement('Amt')
    AmtInstdAmt.setAttribute('Ccy', 'EUR')
    InstdAmt.appendChild(AmtInstdAmt)
    AmtInstdAmtText = doc.createTextNode('%s.00'%AMOUNT)
    AmtInstdAmt.appendChild(AmtInstdAmtText)
    TxAmt=doc.createElement('TxAmt')
    AmtDtls.appendChild(TxAmt)
    AmtInstdAmt2=doc.createElement('Amt')
    AmtInstdAmt2.setAttribute('Ccy', 'EUR')
    TxAmt.appendChild(AmtInstdAmt2)
    AmtInstdAmt2Text = doc.createTextNode('%s.00'%AMOUNT)
    AmtInstdAmt2.appendChild(AmtInstdAmt2Text)
    RltdPties=doc.createElement('RltdPties')
    TxDtls.appendChild(RltdPties)
    Dbtr=doc.createElement('Dbtr')
    RltdPties.appendChild(Dbtr)
    DbtrNm=doc.createElement('Nm')
    Dbtr.appendChild(DbtrNm)
    DbtrNmText = doc.createTextNode(fullname)
    DbtrNm.appendChild(DbtrNmText)
    
    #identity code part
    DbtrID=doc.createElement('Id')
    Dbtr.appendChild(DbtrID)
    id_PrvtId=doc.createElement('PrvtId')
    DbtrID.appendChild(id_PrvtId)
    id_PrvtId_Othr=doc.createElement('Othr')
    id_PrvtId.appendChild(id_PrvtId_Othr)
    id_PrvtId_Othr_id=doc.createElement('Id')
    id_PrvtId_Othr.appendChild(id_PrvtId_Othr_id)
    id_PrvtId_Othr_idText = doc.createTextNode(IDENTITY)
    id_PrvtId_Othr_id.appendChild(id_PrvtId_Othr_idText)
    id_PrvtId_Othr_SchmeNm=doc.createElement('SchmeNm')
    id_PrvtId_Othr.appendChild(id_PrvtId_Othr_SchmeNm)
    id_PrvtId_Othr_SchmeNm_Cd=doc.createElement('Cd')
    id_PrvtId_Othr_SchmeNm.appendChild(id_PrvtId_Othr_SchmeNm_Cd)
    id_PrvtId_Othr_SchmeNm_CdText = doc.createTextNode('NIDN')
    id_PrvtId_Othr_SchmeNm_Cd.appendChild(id_PrvtId_Othr_SchmeNm_CdText)


    ######
    #DbtrAcct
    DbtrAcct=doc.createElement('DbtrAcct')
    RltdPties.appendChild(DbtrAcct)
    DbtrAcctId=doc.createElement('Id')
    DbtrAcct.appendChild(DbtrAcctId)
    DbtrAcctIBAN=doc.createElement('IBAN')
    DbtrAcctId.appendChild(DbtrAcctIBAN)
    DbtrAcctIBANText = doc.createTextNode(IBAN)
    DbtrAcctIBAN.appendChild(DbtrAcctIBANText)
    RltdAgts=doc.createElement('RltdAgts')
    TxDtls.appendChild(RltdAgts)
    DbtrAgt=doc.createElement('DbtrAgt')
    RltdAgts.appendChild(DbtrAgt)
    FinInstnId=doc.createElement('FinInstnId')
    DbtrAgt.appendChild(FinInstnId)
    FinInstnIdBIC=doc.createElement('BIC')
    FinInstnId.appendChild(FinInstnIdBIC)
    FinInstnIdBICText = doc.createTextNode('HABALT22')
    FinInstnIdBIC.appendChild(FinInstnIdBICText)
    
    RmtInf=doc.createElement('RmtInf')
    TxDtls.appendChild(RmtInf)
    Ustrd=doc.createElement('Ustrd')
    RmtInf.appendChild(Ustrd)
    UstrdText = doc.createTextNode(REFNO)
    Ustrd.appendChild(UstrdText)
    Strd=doc.createElement('Strd')
    RmtInf.appendChild(Strd)
    CdtrRefInf=doc.createElement('CdtrRefInf')
    Strd.appendChild(CdtrRefInf)
    Tp=doc.createElement('Tp')
    CdtrRefInf.appendChild(Tp)
    CdOrPrtry=doc.createElement('CdOrPrtry')
    Tp.appendChild(CdOrPrtry)
    Cd=doc.createElement('Cd')
    CdOrPrtry.appendChild(Cd)
    CdText=doc.createTextNode('SCOR')
    Cd.appendChild(CdText)
    #create fle and save it
    xml_str = doc.toprettyxml(indent="  ")
    with open("%s/%s.xml"%(DIRECTORY,unique_filename), "w") as f:
        f.write(xml_str)
#printing user input to the console
def show_entry_fields():
    firstname=e1.get()
    lastname=e2.get()
    fullname=firstname+" "+lastname
    REFNO=e3.get()
    IBAN=e4.get()
    AMOUNT=e5.get()
    print("Full name of customer is"+fullname+" refno is"+REFNO+" IBAN is"+IBAN+" AMOUNT is"+AMOUNT)
   

master = tk.Tk()
tk.Label(master, text="Customer's First Name").grid(row=0)
tk.Label(master, text="Customer's Last Name").grid(row=1)
tk.Label(master, text="REFNO").grid(row=2)
tk.Label(master, text="""IBAN
(can generate with https://bank.codes/iban/generate/lithuania/, Swedbank code is 7300 for example)""").grid(row=3)

tk.Label(master, text="AMOUNT").grid(row=4)
tk.Label(master, text="IDENTITY CODE").grid(row=5)
tk.Label(master, text="Directory where you want to put file").grid(row=6)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)



tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=7,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=7,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
tk.Button(master,
          text='Generate Statement', command=generatestatement).grid(row=7,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()


master = tk.Tk()
