## 目的
- wtformsを使ったお問い合わせフォームの作成について学ぶ
- AppEngineへのCloudBuildを活用したCI/CDの構築
- VScode・GitHub・GCPの3つを連携した開発体制に慣れる
- 暇つぶし

## 完成品を見たい人はこちらから
- ※：裏でGCSが動いているので、個人情報を入力しないでください。
- https://sample-form-404507.an.r.appspot.com/
    - そのうち閉鎖してるかもです。そん時はごめんなさい。

## 特徴
- wtforms候チックしているので、htmlは殆ど書いていません。
- ローカルでも動作するように構築してあります。
    - 環境判別の条件分岐の方法はこちらから。
        - https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app?hl=ja#detecting_application_runtime_environment

## 改善点
- db操作がsqlite3
    - CloudSQLとか、Firestoreの使い方勉強します。。

# 完成イメージ
- 殆ど以下のフレームワークで作成しているハズ…。ご参考までに。
    - ![success-image](https://github.com/sayu349/sample-form-create/tree/main/static/images/sample-form-create.png)