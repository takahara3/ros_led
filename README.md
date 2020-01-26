# ロボットシステム学 2019 課題2
## 概要  
LEDの点滅を行うROSパッケージ.  
入力した数値をrostopicとしてPublishし，別ノードでSubscribeして，入力された回数分LEDを点滅させる．

## 動作環境  
以下の環境で開発，動作確認を行っています．  
* Raspberry Pi  
  - Raspberry Pi Model 3B+  
* OS  
  - Ubuntu 16.04
* LED 　　
  - 赤（大）：22番ピン（GPIO25） 
* ROS  
  - Kinetic Kame

## インストール方法  
### 前処理  
LEDを点滅させるデバイスファイルを作成  
下記リポジトリを用いてデバイスファイルを作成  
https://github.com/takahara3/led_dev.git  
### インストール  

`catkin_ws/src/`内で下記のコマンドを順に実行  

```
$ git clone https://github.com/takahara3/led_ros.git  
$ cd ../  
$ catkin_make
```  
## 実行方法  
* ターミナルを3つ用意し，各ターミナルで下記のコマンドを実行  
ターミナル1  （roscoreの立ち上げ）  
`$ roscore`  
ターミナル2  （入力値をパブリッシュするノード）  
`$ rosrun myros pub_num.py`  
ターミナル3  （トピックをサブスクライブし，回数分LEDを点滅させるノード）  
`$ rosrun myros sub_num.py`    
* ターミナル2にて数値の入力を行うと，その数値の回数LEDが点滅を行う．  

## デモ動画  
https://youtu.be/2gX3uzQG02o  

## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
