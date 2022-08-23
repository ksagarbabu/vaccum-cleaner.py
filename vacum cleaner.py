location=input('enter the current location of the cleaner or agent:')
statusA=int(input('enter the status of Room A:'))
statusB=int(input('enter the status of Room B:'))
cost= 0
if location=='A':
    
    if statusA==1 :
        print('room A is dirty ')
        print('dirty..cleaning  room A')
        print(' Room A cleaned ')
        print('done...')
        cost += 1
        if statusB==1:
            print('The room B is also dirty..')
            print('move right..')
            cost += 1
            print("the room B is cleaned..")
            print('done...')
            cost += 1
        else:
                print('the Room B is already cleaned..')
                print('done..')
                
    else:
            print('the Room A is already cleaned')
            if statusB==1:
                print('The room B is also dirty..')
                print('move right..')
                cost += 1
                print("the room B is cleaned..")
                print('done...')
                cost += 1
            else:
                    print('the Room B is already cleaned..')
                    print('done..')
else:
        if statusB==1:
            print('roomB is dirty')
            print('cleaning room B...')
            print("cleaned ...done")
            cost += 1
            if statusA==1:
                print('The room A is also dirty..')
                print('move left..')
                cost += 1
                print("the room A is cleaned..")
                print('done...')
                cost += 1
            else:
                print('the Room A is already cleaned..')
                print('done..')
                
        else:
            print('the Room b is already cleaned')
            if statusB==1:
                print('The room A is also dirty..')
                print('move right..')
                cost += 1
                print("the room A is cleaned..")
                print('done...')
                cost += 1
            else:
                    print('the Room A is already cleaned..')
                    print('done..')

print('The cost of agent is :',cost)
            
