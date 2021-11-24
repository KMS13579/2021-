
import time
import random
import os
import keyboard

InGameNowPlayerStage = 1
limitMoney = 1500
plusMoney = 1

BitTorrent = {"health": 50, "damage": 2, "defense": 0}
Doge = {"health": 100, "damage": 4, "defense": 10}
Golem = {"health": 150, "damage": 6, "defense": 20}
SandBox = {"health": 200, "damage": 8, "defense": 30}
Elf = {"health": 250, "damage": 10, "defense": 40}
Riple = {"health": 250, "damage": 12, "defense": 50}
Aida = {"health": 300, "damage": 14, "defense": 60}
Solana = {"health": 350, "damage": 16, "defense": 70}
Ethereum = {"health": 400, "damage": 18, "defense": 80}
BitCoin = {"health": 450, "damage": 20, "defense": 90}

class pickWeapon:
    pickCPU = {"i5": 500, "i7": 750, "i9": 10000, "i11": 125000}
    pickGPU = {"970": 500, "1080": 600, "2080": 7000, "3080": 8000}
    pickSSD = {"250": 200, "500": 400, "1T": 800, "2T": 12000}
    pickCPUPercentage = {"i5": 50, "i7": 75, "i9": 100, "i11": 150}
    pickGPUPercentage = {"970": 50, "1080": 60, "2080": 70, "3080": 80}
    pickSSDPercentage = {"250": 5, "500": 10, "1T": 15, "2T": 20}


class deokSang:
    DeokSang = {"healthPoint": 10, "criticalPercentage": 10, "damage": 10}
    deokSSD = ""
    deokGPU = ""
    deokCPU = ""
    money = 0


def fightBoss():
    global hero
    global weapon
    global plusMoney
    global limitMoney

    NowPlayerDamage = hero.DeokSang["damage"]
    NowPlayerHealth = hero.DeokSang["healthPoint"]

    global InGameNowPlayerStage
    NowPlayerStage = InGameNowPlayerStage


    if (NowPlayerStage == 1):
        print("비트토렌트가....나타났다!")
        time.sleep(1)
        NowBitTorrentHealth = BitTorrent["health"]
        NowBitTorrentDefense = BitTorrent["defense"]
        NowBitTorrentDamage = BitTorrent["damage"]

        while(NowBitTorrentHealth > 0):
            NowBitTorrentHealth, NowBitTorrentDefense, NowPlayerDamage = PlayerSelect(NowBitTorrentHealth, NowBitTorrentDefense, NowPlayerDamage)
            if (NowBitTorrentHealth <= 0):
                print("비트토렌트가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 2500
                plusMoney = 10
                hero.DeokSang["healthPoint"] += 30
                print("강해진 느낌이 든다.. 체력이 30 증가했다")
                time.sleep(1)
                hero.money += 600
                print("비트토렌트를 쓰러트리고 600의 돈을 얻었다!")
                time.sleep(1)
                break
            print("비트토렌트가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowBitTorrentDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" %(NowBitTorrentDamage, NowPlayerHealth))
            time.sleep(1)
            if(NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break
        main()

    elif (NowPlayerStage == 2):
        print("도지가....나타났다!")
        time.sleep(1)
        NowDogeHealth = Doge["health"]
        NowDogeDefense = Doge["defense"]
        NowDogeDamage = Doge["damage"]

        while (NowDogeHealth > 0):
            NowDogeHealth, NowDogeDefense, NowPlayerDamage = PlayerSelect(NowDogeHealth,NowDogeDefense, NowPlayerDamage)
            if (NowDogeHealth <= 0):
                print("도지가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 4000
                plusMoney = 50
                hero.DeokSang["healthPoint"] += 35
                print("강해진 느낌이 든다.. 체력이 35 증가했다")
                time.sleep(1)
                hero.money += 900
                print("도지를 쓰러트리고 900의 돈을 얻었다!")
                time.sleep(1)
                break
            print("도지가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowDogeDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowDogeDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 3):
        print("골렘이....나타났다!")
        time.sleep(1)
        NowGolemHealth = Golem["health"]
        NowGolemDefense = Golem["defense"]
        NowGolemDamage = Golem["damage"]

        while (NowGolemHealth > 0):
            NowGolemHealth, NowGolemDefense, NowPlayerDamage = PlayerSelect(NowGolemHealth, NowGolemDefense, NowPlayerDamage)
            if (NowGolemHealth <= 0):
                print("골렘이 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 7000
                plusMoney = 100
                hero.DeokSang["healthPoint"] += 40
                print("강해진 느낌이 든다.. 체력이 40 증가했다")
                time.sleep(1)
                hero.money +=1200
                print("골렘을 쓰러트리고 1200의 돈을 얻었다!")
                time.sleep(1)
                break
            print("골렘이 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowGolemDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowGolemDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 4):
        print("샌드박스가....나타났다!")
        time.sleep(1)
        NowSandBoxHealth = SandBox["health"]
        NowSandBoxDefense = SandBox["defense"]
        NowSandBoxDamage = SandBox["damage"]

        while (NowSandBoxHealth > 0):
            NowSandBoxHealth, NowSandBoxDefense, NowPlayerDamage = PlayerSelect(NowSandBoxHealth, NowSandBoxDefense,
                                                                                NowPlayerDamage)
            if (NowSandBoxHealth <= 0):
                print("샌드박스가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 10000
                plusMoney = 200
                hero.DeokSang["healthPoint"] += 45
                print("강해진 느낌이 든다.. 체력이 45 증가했다")
                time.sleep(1)
                hero.money += 1500
                print("샌드박스를 쓰러트리고 1500의 돈을 얻었다!")
                time.sleep(1)
                break
            print("샌드박스가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowSandBoxDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowSandBoxDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 5):
        print("엘프가....나타났다!")
        time.sleep(1)
        NowElfHealth = Elf["health"]
        NowElfDefense = Elf["defense"]
        NowElfDamage = Elf["damage"]

        while (NowElfHealth > 0):
            NowElfHealth, NowElfDefense, NowPlayerDamage = PlayerSelect(NowElfHealth, NowElfDefense,
                                                                                 NowPlayerDamage)
            if (NowElfHealth <= 0):
                print("엘프가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 15000
                plusMoney = 250
                hero.DeokSang["healthPoint"] += 50
                print("강해진 느낌이 든다.. 체력이 50 증가했다")
                time.sleep(1)
                hero.money += 8350
                print("엘프를 쓰러트리고 8350의 돈을 얻었다!")
                time.sleep(1)
                break
            print("엘프가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowElfDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowElfDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 6):
        print("리플이....나타났다!")
        time.sleep(1)

        NowRipleHealth = Riple["health"]
        NowRipleDefense = Riple["defense"]
        NowRipleDamage = Riple["damage"]

        while (NowRipleHealth > 0):
            NowRipleHealth, NowRipleDefense, NowPlayerDamage = PlayerSelect(NowRipleHealth, NowRipleDefense,
                                                                         NowPlayerDamage)
            if (NowRipleHealth <= 0):
                print("리플이 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 20000
                plusMoney = 500
                hero.DeokSang["healthPoint"] += 55
                print("강해진 느낌이 든다.. 체력이 55 증가했다")
                time.sleep(1)
                hero.money += 10000
                print("리플을 쓰러트리고 10000의 돈을 얻었다!")
                time.sleep(1)
                break
            print("리플이 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowRipleDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowRipleDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 7):
        print("에이다가....나타났다!")
        time.sleep(1)
        NowAidaHealth = Aida["health"]
        NowAidaDefense = Aida["defense"]
        NowAidaDamage = Aida["damage"]

        while (NowAidaHealth > 0):
            NowAidaHealth, NowAidaDefense, NowPlayerDamage = PlayerSelect(NowAidaHealth, NowAidaDefense,
                                                                           NowPlayerDamage)
            if (NowAidaHealth <= 0):
                print("에이다가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 30000
                plusMoney = 750
                hero.DeokSang["healthPoint"] += 60
                print("강해진 느낌이 든다.. 체력이 60 증가했다")
                time.sleep(1)
                hero.money += 17000
                print("에이다를 쓰러트리고 17000의 돈을 얻었다!")
                time.sleep(1)
                break
            print("에이다가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowAidaDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowAidaDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break

    elif (NowPlayerStage == 8):
        print("솔라나가....나타났다!")
        time.sleep(1)
        NowSolanaHealth = Aida["health"]
        NowSolanaDefense = Aida["defense"]
        NowSolanaDamage = Aida["damage"]

        while (NowSolanaHealth > 0):
            NowSolanaHealth, NowSolanaDefense, NowPlayerDamage = PlayerSelect(NowSolanaHealth, NowSolanaDefense,
                                                                              NowPlayerDamage)
            if (NowSolanaHealth <= 0):
                print("솔라나가 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 45000
                plusMoney = 800
                hero.DeokSang["healthPoint"] += 65
                print("강해진 느낌이 든다.. 체력이 65 증가했다")
                time.sleep(1)
                hero.money += 43000
                print("솔라나를 쓰러트리고 43000의 돈을 얻었다!")
                time.sleep(1)
                break
            print("솔라나가 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowSolanaDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowSolanaDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break
    elif (NowPlayerStage == 9):
        print("이더리움이....나타났다!")
        time.sleep(1)
        NowEthereumHealth = Aida["health"]
        NowEthereumDefense = Aida["defense"]
        NowEthereumDamage = Aida["damage"]

        while (NowEthereumHealth > 0):
            NowEthereumHealth, NowEthereumDefense, NowPlayerDamage = PlayerSelect(NowEthereumHealth, NowEthereumDefense,
                                                                              NowPlayerDamage)
            if (NowEthereumHealth <= 0):
                print("이더리움이 쓰러졌다")
                time.sleep(1)
                InGameNowPlayerStage += 1
                limitMoney = 1000000
                plusMoney = 2000
                hero.DeokSang["healthPoint"] += 70
                print("강해진 느낌이 든다.. 체력이 70 증가했다")
                time.sleep(1)
                hero.money += 43000
                print("솔라나를 쓰러트리고 70000의 돈을 얻었다!")
                time.sleep(1)
                break
            print("이더리움이 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowEthereumDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowEthereumDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break
    elif (NowPlayerStage == 10):
        print("비트코인이....나타났다!")
        time.sleep(1)
        NowBitCoinHealth = Aida["health"]
        NowBitCoinDefense = Aida["defense"]
        NowBitCoinDamage = Aida["damage"]

        while (NowBitCoinHealth > 0):
            NowBitCoinHealth, NowBitCoinDefense, NowPlayerDamage = PlayerSelect(NowBitCoinHealth, NowBitCoinDefense,
                                                                              NowPlayerDamage)
            if (NowBitCoinHealth <= 0):
                print("비트코인이 쓰러졌다")
                time.sleep(1)
                end()
                break
            print("비트코인이 공격했다!")
            time.sleep(1)
            NowPlayerHealth -= NowBitCoinDamage
            print("덕상은 %d의 피해를 받아 %d의 체력이 됬다!" % (NowBitCoinDamage, NowPlayerHealth))
            time.sleep(1)
            if (NowPlayerHealth <= 0):
                print("덕상의 눈 앞이 깜깜해졌다.....")
                time.sleep(1)
                break


def PlayerSelect(NowBossHealth, NowBossDefense, NowPlayerDamage):
    global hero
    global weapon
    print("")
    print("무슨행동을 할까?")
    action = input("1.일반공격 / 2.스킬")
    CpuCalculation = 1.0
    GpuCalculation = hero.DeokSang["criticalPercentage"]
    SSDCalculation = hero.DeokSang["damage"]

    if (hero.deokCPU != ""):
        CpuCalculation = ((weapon.pickCPUPercentage[hero.deokCPU]+100)/100)
    if(hero.deokGPU != ""):
        GpuCalculation = weapon.pickGPUPercentage[hero.deokGPU]
    if(hero.deokSSD != ""):
        SSDCalculation = weapon.pickSSDPercentage[hero.deokSSD]


    if ((action == "일반공격") or (action == "1")):
        criticalPercent = random.randint(1, 10)
        if (GpuCalculation-(10*criticalPercent) >= 0):
            if ((2*(CpuCalculation*SSDCalculation))== NowBossDefense):
                print("적의 방어력이 높아 크리티컬 공격이 통하지 않는다!")
                time.sleep(1)
            else:
                print("크리티컬! %d의 데미지를 주었다." % (2*(CpuCalculation*SSDCalculation)))
                time.sleep(1)
                NowBossHealth = NowBossHealth - (2*(CpuCalculation*SSDCalculation)-NowBossDefense)
                print("보스의 체력은 %d가 되었다!" % NowBossHealth)
                time.sleep(1)
        else:
            if ((CpuCalculation*SSDCalculation)== NowBossDefense):
                print("적의 방어력이 높아 공격이 통하지 않는다!")
                time.sleep(1)
            else:
                print("%d의 데미지를 주었다." %(CpuCalculation*SSDCalculation))
                time.sleep(1)
                NowBossHealth = NowBossHealth -((CpuCalculation*SSDCalculation)-NowBossDefense)
                print("보스의 체력은 %d이 되었다!" % NowBossHealth)
                time.sleep(1)

        return NowBossHealth, NowBossDefense, NowPlayerDamage
    elif ((action == "스킬") or (action == "2")):
        print("사용할 스킬을 고르세요")
        skill = input("1. 상승장(내 공격력 업) / 2. 하락장(상대 방어력 다운)")

        if ((skill == "상승장")or (skill == "1")):
            NowPlayerDamage = NowPlayerDamage + 5
            print("덕상의 공격력이 5상승해 %d가 되었다." % NowPlayerDamage)
            time.sleep(1)
        elif ((skill == "하락장")or (skill == "2")):
            NowBossDefense = NowBossDefense - 5
            print("보스의 방어력이 5하락해 %d가 되었다." %NowBossDefense)
            time.sleep(1)
        else:
            print("스킬을 잘못 사용했다!..아무런일도 일어나지 않았다!")
            time.sleep(1)
    else:
        print("이 선택은 잘못된것 같다...")
        time.sleep(1)
        NowBossHealth, NowBossDefense, NowPlayerDamage = PlayerSelect(NowBossHealth, NowBossDefense, NowPlayerDamage)

    return NowBossHealth, NowBossDefense, NowPlayerDamage


def buyCPU(money):
    global hero
    global weapon
    print("구매하고 싶은 무기를 골라주세요")
    print("무기 : ", list(weapon.pickCPU.keys()))
    print("가격 : ", list(weapon.pickCPU.values()))
    pick = input("무기 선택 : ")

    if pick in weapon.pickCPU:
        if hero.money >= weapon.pickCPU[pick]:
            hero.money -= weapon.pickCPU.get(pick)
            hero.deokCPU = pick
            del(weapon.pickCPU[pick])
        else :
            print("돈이 부족합니다 돈을 모아주세요.")
            time.sleep(1)
            main()
    else :
        print("그 무기는 상점에 없습니다.")
        print("다시 골라주세요.")
        time.sleep(1)
        buyCPU(money)
    return hero.money, weapon.pickCPU

def buyGPU(money):
    global hero
    global weapon
    print("구매하고 싶은 무기를 골라주세요")
    print("무기 : ", list(weapon.pickGPU.keys()))
    print("가격 : ", list(weapon.pickGPU.values()))
    pick = input("무기 선택 : ")

    if pick in weapon.pickGPU :
        if hero.money >= weapon.pickGPU[pick]:
            hero.money -= weapon.pickGPU.get(pick)
            hero.deokGPU = pick
            del(weapon.pickGPU[pick])
        else :
            print("돈이 부족합니다 돈을 모아주세요.")
            time.sleep(1)
            main()
    else :
        print("그 무기는 상점에 없습니다.")
        print("다시 골라주세요.")
        time.sleep(1)
        buyGPU(money)

    return hero.money, weapon.pickGPU

def buySSD(money):
    global hero
    global weapon
    print("구매하고 싶은 무기를 골라주세요")
    print("무기 : ", list(weapon.pickSSD.keys()))
    print("가격 : ", list(weapon.pickSSD.values()))
    pick = input("무기 선택 : ")

    if pick in weapon.pickSSD :
        if hero.money >= weapon.pickSSD[pick]:
            hero.money -= weapon.pickSSD.get(pick)
            hero.deokSSD = pick
            del(weapon.pickSSD[pick])
        else :
            print("돈이 부족합니다 돈을 모아주세요.")
            print()
            time.sleep(1)
            main()
    else :
        print("그 무기는 상점에 없습니다.")
        print("다시 골라주세요.")
        print()
        time.sleep(1)
        buySSD(money)

    return hero.money, weapon.pickSSD

def EarnMoney():
    global hero
    global limitMoney
    global plusMoney

    print("***********채굴장***********")
    print("Z를 누르면 돈을 벌 수 있습니다.")
    print("S를 눌러 메인화면으로 갈 수 있습니다.")
    print("이제 Z키를 눌러 돈을 벌어보세요!!")
    print()

    while 1 :
        if hero.money >= limitMoney :
            print()
            hero.money = hero.money - (hero.money-limitMoney)
            print("벌 수 있는 금액을 초과하였습니다.")
            time.sleep(1)
            print("다음 보스를 잡아 벌 수 있는 금액을 늘려주세요.")
            time.sleep(1)
            print("현재 자산 : ", hero.money)
            time.sleep(1)
            print()
            return hero.money

        if keyboard.read_key() == "s":
            print()
            print("현재 자산 : ", hero.money)
            time.sleep(1)
            return hero.money

        if keyboard.read_key() == "z":
            print()
            print(plusMoney, "원 만큼 돈을 벌었다!")
            hero.money += plusMoney
            print("현재 자산 : ", hero.money)
            print()
        else :
            print()
            print("Z를 눌러 주세요")

def main():
        print("**********************")
        print("1. CPU상점\n2.GPU상점\n3. SSD상점\n4. 자산확인\n5. 전투\n6.장비확인 \n7. 돈벌기")
        print("**********************")
        choice = input("무엇을 할까? ")
        if choice == "1":
            time.sleep(1)
            print("\n\n\n")
            buyCPU(hero.money)
            main()
        elif choice == "2":
            time.sleep(1)
            print("\n\n\n")
            buyGPU(hero.money)
            main()
        elif choice == "3":
            time.sleep(1)
            print("\n\n\n")
            buySSD(hero.money)
            main()
        elif choice == "4":
            time.sleep(1)
            time.sleep(0.5)
            print("현재 자산 : ", hero.money)
            time.sleep(1)
            print("\n")
            main()
        elif choice == "5":
            time.sleep(1)
            print("\n\n\n")
            fightBoss()
            main()
        elif choice == "6":
            time.sleep(1)
            print("\n\n\n")
            print(hero.deokCPU)
            print(hero.deokGPU)
            print(hero.deokSSD)
            print("\n")
            time.sleep(1)
            main()
        elif choice == "7":
            time.sleep(1)
            print("\n\n")
            EarnMoney()
            main()
        else:
            time.sleep(1)
            print("\n\n\n")
            main()


def end():
    print("결국...덕상은 비트코인나라를 정복하고, 모든 나라를 대통합한다.  덕상의 꿈은 이세계에서 이루어진 것이다.\n")
    time.sleep(2)
    input("계속하려면 아무키나 입력하세요\n")
    time.sleep(2)
    print("하지만...결국 잠은 잠이였고, 덕상은 꿈이란 것을 알아버리고 모두 덧없음을 알아버리고 공장에 입사한다. 여러분도 헛된 희망을 갖지말고 열심히 일을 해보는 것은 어떨까요?\n")
    time.sleep(2)
    input("계속하려면 아무키나 입력하세요")

hero = deokSang()
weapon = pickWeapon()


print("때는 2020년... 많은 이들이 코인에 뛰어든다.\n")
time.sleep(2)
print("그곳에는 우리의 주인공 덕상 역시 끼어있었는데 덕상은 결국 빠져나오지 못하고 망함의 길로 빠져들고 만다...\n")
time.sleep(2)
print("그리고 어느날, 깊은 잠에서 깨어나지 못하는 덕상이였는데..... \n")
time.sleep(2)
print("그리고 눈을 떠보니...덕상은 이세계! 코인나라에 도착해있었다!\n")
time.sleep(2)

input("계속하려면 아무키나 입력하세요")
print("\n\n\n\n\n\n")

main()

