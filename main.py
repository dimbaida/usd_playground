from pxr import Usd


stage: Usd.Stage = Usd.Stage.Open('usd_models/transforms_issue.prime.usda')
prim: Usd.Prim = stage.GetPrimAtPath('/meshes')

i: Usd.Prim
children = prim.GetChildren()
