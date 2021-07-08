# Add the functions in this file
import json

def load_journal(file:str)->dict:
    fptr=open(file,"r")
    ret=json.load(fptr)
    return ret

def compute_phi(file:str, exist:str)->float:
    ret=load_journal(file)
    corr=0.0
    n00=n11=n01=n10=0
    n_0=n_1=n1_=n0_=0

    for i in range(len(ret)):
        sq=dict(ret[i])['squirrel']
        eve=dict(ret[i])['events']

        if sq==True:
            n_1+=1
        else:
            n_0+=1
        
        if exist in eve:
            n1_+=1
            if sq:
                n11+=1
            else:
                n10+=1
        else:
            n0_+=1
            if sq:
                n01+=1
            else:
                n00+=1

    corr=(n11*n00 -n01*n10)/((n_1*n_0*n0_*n1_)**0.5)
    return corr


def compute_correlations(file:str)->dict:
    ret=load_journal(file)
    event_dic={}

    for i in range(len(ret)):
        eve=ret[i]["events"]
        for j in eve:
            if j not in event_dic:
                event_dic[j]=compute_phi(file,j)
    return event_dic

def diagnose(file: str) -> dict:
    event_dic = compute_correlations(file)
    ret = []

    Max,Min = -999,999
    max_event,min_event = "",""

    for i in event_dic:
        if(event_dic[i]<Min):
            Min = event_dic[i]
            min_event = i
        elif(event_dic[i]>Max):
            Max = event_dic[i]
            max_event = i

    ret.append(max_event)
    ret.append(min_event)

    return ret