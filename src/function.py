import numpy as np

def get_onehot(haipai_list):
    eye = np.eye(27)
    temp = []
    for haipai in haipai_list:
        onehot = eye[haipai]
        temp.append(onehot)
    np_temp = np.array(temp)
    return np_temp

def flatten(haipai_list_np):
    list = []
    for n in range(haipai_list_np.shape[0]):
        list.append(haipai_list_np[n].reshape(-1))
    return np.array(list)

sanma_pai_to_num = {'1m': 0, '9m': 1, 
'1p': 2, '2p': 3, '3p': 4, '4p': 5, '5p': 6, '6p': 7, '7p': 8, '8p': 9, '9p': 10, 
'1s': 11, '2s': 12, '3s': 13, '4s': 14, '5s': 15, '6s': 16, '7s': 17, '8s': 18, '9s': 19, 
'東': 20, '南': 21, '西': 22, '北': 23, '白': 24, '撥': 25, '中': 26}

jihai_dict = {'1':'東', '2':'南', '3':'西', '4':'北', '5':'白', '6':'撥', '7':'中'}

def split_pai(pai):

    dummy = [char for char in pai]
    m_list, p_list, s_list, z_list = [], [], [], []
    pre = []
    for char in dummy:
        if (char != 'm') and (char != 'p') and (char != 's') and (char != 'z'):
            pre.append(char)
        
        elif char == 'm':
            m_pre = [sanma_pai_to_num[char + 'm'] for char in pre]
            m_list += m_pre
            pre = []
        
        if char == 'p':
            p_pre = [sanma_pai_to_num[char + 'p'] for char in pre]
            p_list += p_pre
            pre = []

        elif char == 's':
            s_pre = [sanma_pai_to_num[char + 's'] for char in pre]
            s_list += s_pre
            pre = []
            
        elif char == 'z':
            z_pre = [sanma_pai_to_num[jihai_dict[char]] for char in pre]
            z_list += z_pre
            pre = []
        
        pai_list = m_list + p_list + s_list + z_list
    return pai_list