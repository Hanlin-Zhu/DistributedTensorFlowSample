# DistributedTensorFlowSample

Distributed TensorFlow のサンプルです。

grpc_tensorflow_serverがビルドされており、パスも通っている環境で動作します。

説明は近々Qiitaに書きます。

## シングルCPU版の実行

```
python ./single_cpu.py
```

## モデル並列版の実行

```
./model_parallel_server.sh
python ./model_parallel.py
```

## データ並列版の実行

```
./data_parallel_server.sh
python ./single_cpu.py
```

