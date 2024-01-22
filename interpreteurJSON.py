import json



class StatSiege():
    information_a_passer = []

    def __init__(self):
        json_file_path = "SiegeMatch3.json"
        with open(json_file_path, 'r', encoding="utf8") as j:
            self.contents = json.loads(j.read())

    def stats(self):

        print("-------------------------------------------------------------------------------------------------------------------------")
        guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["guild_name"]
        print(json.dumps(guild1))
        guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["guild_name"]
        print(json.dumps(guild2))
        guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["guild_name"]
        print(json.dumps(guild3))
        print("-------------------------------------------------------------------------------------------------------------------------")
        nb_attaque_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["attack_count"]
        nb_player_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["play_member_count"]
        nb_attaque_possible_guild1 = nb_player_guild1*10
        ratio_attaque_guild1 = (nb_attaque_guild1/nb_attaque_possible_guild1)*100
        end_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["match_score"]
        info1 = (guild1)+" : "+ str(nb_attaque_guild1)+" soit un ratio de "+str(ratio_attaque_guild1)+"%,           fini à "+str(end_guild1)
        print(info1)
        #-------------------------------------------------------------------------------------------------------------------------
        nb_attaque_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["attack_count"]
        nb_player_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["play_member_count"]
        nb_attaque_possible_guild2 = nb_player_guild2*10
        ratio_attaque_guild2 = (nb_attaque_guild2/nb_attaque_possible_guild2)*100
        end_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["match_score"]
        info2 = (guild2)+" : "+ str(nb_attaque_guild2)+" soit un ratio de "+str(ratio_attaque_guild2)+"%,           fini à "+str(end_guild2)
        print(info2)
        #-------------------------------------------------------------------------------------------------------------------------
        nb_attaque_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["attack_count"]
        nb_player_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["play_member_count"]
        nb_attaque_possible_guild3 = nb_player_guild3*10.0
        ratio_attaque_guild3 = (nb_attaque_guild3/nb_attaque_possible_guild3)*100
        end_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["match_score"]
        info3 = (guild3)+" : "+ str(nb_attaque_guild3)+" soit un ratio de "+str(ratio_attaque_guild3)+"%,           fini à "+str(end_guild3)
        print(info3)
        #-------------------------------------------------------------------------------------------------------------------------

        self.information_a_passer = []
        self.information_a_passer.append(info1)
        self.information_a_passer.append(info2)
        self.information_a_passer.append(info3)
        info_index = 3

        print("-------------------------------------------------------------------------------------------------------------------------")
        battle_log = self.contents["attack_log"]["log_list"][0]["battle_log_list"]
        nombre_victoire_total = 0
        nombre_combat_total = 0
        wizard = []
        nombre_combats = []
        nombre_victoire = []
        for i in range(len(battle_log)):
            if(battle_log[i]["wizard_name"] not in wizard):
                wizard.append(battle_log[i]["wizard_name"])
                index_wizard = wizard.index(battle_log[i]["wizard_name"])

                nombre_combats.append(1)
                if(battle_log[i]["win_lose"] == 1):
                    nombre_victoire.append(1)
                    nombre_victoire_total +=1
                    nombre_combat_total += 1
                else:
                    nombre_victoire.append(0)
                    nombre_combat_total+=1
            else:
                index_wizard = wizard.index(battle_log[i]["wizard_name"])

                nombre_combats[index_wizard] += 1
                if(battle_log[i]["win_lose"] == 1):
                    nombre_victoire[index_wizard] +=1


        for k in range(len(wizard)):
            winrate = (nombre_victoire[k]/nombre_combats[k])*100

            info = wizard[k]+" : "+str(nombre_combats[k])+", winrate de "+str(winrate)+"%"
            self.information_a_passer.append(info)

        self.information_a_passer.append("--------------------------------------------------------------------------------------")
        winrate_total = (nombre_victoire_total/nombre_combat_total)*100
        self.information_a_passer.append("Winrate de la guilde = "+str(winrate_total)+"%")
        
        return self.information_a_passer

    def statsDefense(self):
        print("-------------------------------------------------------------------------------------------------------------------------")
        guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["guild_name"]
        print(json.dumps(guild1))
        guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["guild_name"]
        print(json.dumps(guild2))
        guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["guild_name"]
        print(json.dumps(guild3))
        print("-------------------------------------------------------------------------------------------------------------------------")
        nb_attaque_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["attack_count"]
        nb_player_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["play_member_count"]
        nb_attaque_possible_guild1 = nb_player_guild1*10
        ratio_attaque_guild1 = (nb_attaque_guild1/nb_attaque_possible_guild1)*100
        end_guild1 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][0]["match_score"]
        info1 = (guild1)+" : "+ str(nb_attaque_guild1)+" soit un ratio de "+str(ratio_attaque_guild1)+"%,           fini à "+str(end_guild1)
        print(info1)
        #-------------------------------------------------------------------------------------------------------------------------
        nb_attaque_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["attack_count"]
        nb_player_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["play_member_count"]
        nb_attaque_possible_guild2 = nb_player_guild2*10
        ratio_attaque_guild2 = (nb_attaque_guild2/nb_attaque_possible_guild2)*100
        end_guild2 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][1]["match_score"]
        info2 = (guild2)+" : "+ str(nb_attaque_guild2)+" soit un ratio de "+str(ratio_attaque_guild2)+"%,           fini à "+str(end_guild2)
        print(info2)
        #-------------------------------------------------------------------------------------------------------------------------
        nb_attaque_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["attack_count"]
        nb_player_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["play_member_count"]
        nb_attaque_possible_guild3 = nb_player_guild3*10.0
        ratio_attaque_guild3 = (nb_attaque_guild3/nb_attaque_possible_guild3)*100
        end_guild3 = self.contents["attack_log"]["log_list"][0]["guild_info_list"][2]["match_score"]
        info3 = (guild3)+" : "+ str(nb_attaque_guild3)+" soit un ratio de "+str(ratio_attaque_guild3)+"%,           fini à "+str(end_guild3)
        print(info3)
        #-------------------------------------------------------------------------------------------------------------------------

        self.information_a_passer = []
        self.information_a_passer.append(info1)
        self.information_a_passer.append(info2)
        self.information_a_passer.append(info3)
        info_index = 3

        print("-------------------------------------------------------------------------------------------------------------------------")
        battle_log_defense = self.contents["defense_log"]["log_list"][0]["battle_log_list"]

        total_defense = 0
        defense_guild2 = 0
        defense_guild3 = 0
        info = []

        for i in range(len(battle_log_defense)):
            if(battle_log_defense[i]["opp_guild_name"] == guild2):
                defense_guild2 += 1
            if(battle_log_defense[i]["opp_guild_name"] == guild3):
                defense_guild3 += 1
        total_defense = defense_guild2+defense_guild3

        ratio_guild2 = (defense_guild2/total_defense)*100
        ratio_guild3 = (defense_guild3/total_defense)*100

        ratio_guild2 = float("{:.2f}".format(ratio_guild2))
        ratio_guild3 = float("{:.2f}".format(ratio_guild3))

        info.append("Defense pris par "+str(guild2)+" : "+str(defense_guild2)+", un ratio de "+str(ratio_guild2)+"% sur nous")
        info.append("Defense pris par "+str(guild3)+" : "+str(defense_guild3)+", un ratio de "+str(ratio_guild3)+"% sur nous")

        focus1 = (defense_guild2/nb_attaque_guild2)*100
        focus2 = (defense_guild2/nb_attaque_guild3)*100

        focus1 = float("{:.1f}".format(focus1))
        focus2 = float("{:.1f}".format(focus2))

        info.append("-----------------------------------------------------------------------------------")
        if(focus1 >= 70):
            info.append(str(guild2)+" nous a focus à "+str(focus1)+"%  <---------- grosse pute")
        else:
            info.append(str(guild2)+" nous a focus à "+str(focus1)+"%")
        if(focus2 >= 70):
            info.append(str(guild3)+" nous a focus à "+str(focus2)+"%  <---------- grosse pute")
        else:
            info.append(str(guild3)+" nous a focus à "+str(focus2)+"%")

        return info