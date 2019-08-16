
"""
Created on Sun Mar 10 11:53:23 2019

@author: hkujawska
"""
from random import randrange, randint, seed
import numpy as np
import pandas as pd
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement # for Dodgson winner
import matplotlib.pyplot as plt


class DB (object):
    '''
    Create balanced DB
    '''
    
    def __init__(self, numCand, numVotes, numProfiles):
        self.numCand = numCand        # number of alternatives (candidates)
        self.numVotes = numVotes      # number of preferences (ranks/votes)
        self.numProfiles = numProfiles  # number of agents (voters)
		
    def createProfile(self):
        '''
        this function will create the profile from given matrix of ranks choices
        '''
        profile = []
        #create permutation
        t = np.arange(1,self.numCand +1) # set of candidates
        [profile.append(np.random.RandomState(seed=43).permutation(t)) for element in range(self.numVotes)]
        return pd.DataFrame([profile])
    
    def createTensorRepresentation(self):
        '''
        this function create the tensor  version representation
        features: each voter
        value of the feature: voter ranking
        '''
  
        tensorRepresentation= pd.DataFrame()
        
        for profileRow in range(self.numProfiles):
            tensorRepresentation = tensorRepresentation.append(self.createProfile())
        return tensorRepresentation.reset_index(drop=True)


    
''' 
--------Borda Winner---------
'''
class Borda():
    
    def __init__(self, representation):
        self.listOfCand = sorted(representation[0][0])
        self.profiles = representation 
        
    
    def CalculateWinner(self):
        '''
        this function calculates borda winner and create new data frame with features.         
        input:  profile - data frame (profiles). Cell is rank. Observation is profile.
        output: winner - column (numCand x 1)  with list of Borda winners, i.e.
                         candidate(s) number(s)
                dfNewFeatures1 - dataframe with new features. 
                        Features (columns) names are the candidates names,
                        the feature's value are Borda scores
                AnimousRepresentation - original dataset with ranks and joined the BordaWinner column                         
        '''
        
        winner=[]
        dfNewFeatures1=pd.DataFrame()
        
        for row in range(self.profiles.shape[0]):
            '''
            Converting a list to dictionary with list elements as keys in dictionary
            All keys will have same value
            ''' 
            dictOfBordaScores = { i : 0 for i in self.listOfCand } #clear dictionary
            for col in range(self.profiles.shape[1]): # 6 last are targets columns
                rank = self.profiles.iloc[row][col]
                for position in range(len(rank)):
                    score = self.listOfCand[-position-1] - 1 #pos1:29, pos2:28, pos3:27...
                    key = int(rank[position])
                    dictOfBordaScores[key]+=score
                    #print('position', position,'score', score , 'key',key,'dictOfBordaScores[key]',dictOfBordaScores[key] )
            dfNewFeatures = pd.DataFrame(list(dictOfBordaScores.values())).transpose()
            dfNewFeatures.columns =  self.listOfCand
            '''Get all candidates wih max value of points'''
            
            BordaWinner=[]
            [BordaWinner.append(el) for el in range(1,len(self.listOfCand)+1) if dfNewFeatures.iloc[0][el] ==dfNewFeatures.iloc[0][:len(self.listOfCand)].max()]
            dfNewFeatures['BordaWinner'] = pd.DataFrame([[BordaWinner]])    
        
            dfNewFeatures1 = pd.concat([dfNewFeatures1,dfNewFeatures]).reset_index(drop=True)
        AnimousRepresentation = self.profiles.join(dfNewFeatures1['BordaWinner'])
        return dfNewFeatures1['BordaWinner'], dfNewFeatures1, AnimousRepresentation


'''
Main part
'''
numCand =20
numVotes =25
numProfiles =12360

#generate synthetic DB
Dataset = DB(numCand, numVotes, numProfiles)
profile = Dataset.createProfile()
BordaWinner, _, representation1 = Borda(profile).CalculateWinner()

representation = pd.DataFrame (Dataset.createTensorRepresentation())
BordaDataset = Borda(representation)
BordaWinner, BordaRepresentation, OriginalDataset = BordaDataset.CalculateWinner()

ListOfStr = [str(el) for el in BordaWinner.tolist()]
BordaRepresentation['BordaWinner'] = ListOfStr
from itertools import groupby, dropwhile
freq = np.array([len(list(group)) for key, group in groupby(sorted(ListOfStr)) if len(key)<6])
key = np.array([key for key, group in groupby(sorted(ListOfStr)) if len(key)<6])
rb = np.round((Dataset.numProfiles/Dataset.numCand))# ratio balanced
while (freq < rb).any()==True:

    profile = Dataset.createProfile()
    BordaWinner, BordaRepresentationProfile, OriginalDatasetProfile = Borda(profile).CalculateWinner()

    BordaRepresentation = BordaRepresentation.append(BordaRepresentationProfile).reset_index(drop=True)
    OriginalDataset = OriginalDataset.append(OriginalDatasetProfile).reset_index(drop=True)
    ListOfStr = [str(el) for el in BordaRepresentation['BordaWinner'].tolist()]
    BordaRepresentation['BordaWinner'] = ListOfStr
    freq = np.array([len(list(group)) for key, group in groupby(sorted(ListOfStr)) if len(key)<6])
    key = np.array([key for key, group in groupby(sorted(ListOfStr)) if len(key)<6])
    #print('freq',freq, 'Ratio Balanced:', np.round((Dataset.numProfiles/Dataset.numCand)), freq<rb, key)

##FinalDB
FinalDB = pd.DataFrame()
OriginalFinalDB= pd.DataFrame()
OriginalDataset['BordaWinner'] = ListOfStr
for winner, label in enumerate(key):
    WinnerFinalDB = BordaRepresentation.loc[BordaRepresentation['BordaWinner']==key[winner]][:int(rb)]
    FinalDB = FinalDB.append(WinnerFinalDB)

    OriginalWinnerFinalDB = OriginalDataset.loc[OriginalDataset['BordaWinner']==key[winner]][:int(rb)]
    OriginalFinalDB = OriginalFinalDB.append(OriginalWinnerFinalDB)
    
# convert labels form list -> int
OriginalFinalDB['BordaWinner'] = [eval(FinalDB['BordaWinner'].loc[el])[0] for el in FinalDB['BordaWinner'].index]
FinalDB['BordaWinner'] = OriginalFinalDB['BordaWinner']

print('FinalDB Borda Representation: \n',FinalDB.sort_index())
print('FinalDB Original Representation: \n',OriginalFinalDB)


#check
print('Check:\n',FinalDB['BordaWinner'].value_counts())
