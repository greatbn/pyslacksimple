#####PySlackSimple

- Get token of your slack domain at: https://api.slack.com/docs/oauth-test-tokens

- Set environment variable 
```sh
export SLACK_TOKEN=your_token
```

- Get data

```sh
saphi@saphi-kma ~/Github/pyslacksimple/client $ python __init__.py 
+-----------+--------------+-------------------+---------+------------------------------------------------------------------------------------------------------------+
|     ID    | Channel Name | Number of Members | Creator |                                                   Topic                                                    |
+-----------+--------------+-------------------+---------+------------------------------------------------------------------------------------------------------------+
| C0FGYCMT7 |   boy_girl   |         10        |  saphi  |                                                                                                            |
| C1HT6RQF5 |   chemgio    |         4         |  saphi  |                                                                                                            |
| C1E4WJL3H | dbot_checker |         8         |  saphi  |                                                                                                            |
| C1DFLKY5A |   forensic   |         8         |  saphi  |                                                                                                            |
| C0AJ904BV |   general    |         33        |  saphi  |                             Company-wide announcements and work-based matters                              |
| C0F32L1UJ |   program    |         22        |  saphi  | Tài liệu python cơ bản: http://ksec.info/threads/python-tong-hop-cau-hoi-thac-mac-va-chia-se-tai-lieu.569/ |
| C0AJ904CB |    random    |         30        |  saphi  |                               Non-work banter and water cooler conversation                                |
| C1DA0J2BS |   security   |         10        |  saphi  |                                                                                                            |
| C1NJEL3EZ |     url      |         4         |  saphi  |                                                                                                            |
+-----------+--------------+-------------------+---------+------------------------------------------------------------------------------------------------------------+

```
