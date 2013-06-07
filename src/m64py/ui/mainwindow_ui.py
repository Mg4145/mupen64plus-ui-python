# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun  7 18:55:40 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 289)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuLoad = QtGui.QMenu(self.menuFile)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        self.menuRecent = QtGui.QMenu(self.menuFile)
        self.menuRecent.setObjectName(_fromUtf8("menuRecent"))
        self.menuStateSlot = QtGui.QMenu(self.menuFile)
        self.menuStateSlot.setObjectName(_fromUtf8("menuStateSlot"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setSeparatorsCollapsible(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEmulation = QtGui.QMenu(self.menubar)
        self.menuEmulation.setObjectName(_fromUtf8("menuEmulation"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuWindowSize = QtGui.QMenu(self.menuView)
        self.menuWindowSize.setObjectName(_fromUtf8("menuWindowSize"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet(_fromUtf8("QStatusBar::item { border: 0px solid; }\n"
"QStatusBar { margin:0px; }"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionManually = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_open_manually.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManually.setIcon(icon1)
        self.actionManually.setObjectName(_fromUtf8("actionManually"))
        self.actionFromList = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_open_from_list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFromList.setIcon(icon2)
        self.actionFromList.setObjectName(_fromUtf8("actionFromList"))
        self.actionKeyboard = QtGui.QAction(MainWindow)
        self.actionKeyboard.setObjectName(_fromUtf8("actionKeyboard"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionClearHistory = QtGui.QAction(MainWindow)
        self.actionClearHistory.setEnabled(False)
        self.actionClearHistory.setObjectName(_fromUtf8("actionClearHistory"))
        self.actionPaths = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_paths.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaths.setIcon(icon4)
        self.actionPaths.setObjectName(_fromUtf8("actionPaths"))
        self.actionGraphic = QtGui.QAction(MainWindow)
        self.actionGraphic.setObjectName(_fromUtf8("actionGraphic"))
        self.actionEmulator = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_emulator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEmulator.setIcon(icon5)
        self.actionEmulator.setObjectName(_fromUtf8("actionEmulator"))
        self.actionPlugins = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_plugins.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlugins.setIcon(icon6)
        self.actionPlugins.setObjectName(_fromUtf8("actionPlugins"))
        self.actionLicense = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_license.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLicense.setIcon(icon7)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.actionLoadState = QtGui.QAction(MainWindow)
        self.actionLoadState.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_state_load.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadState.setIcon(icon8)
        self.actionLoadState.setObjectName(_fromUtf8("actionLoadState"))
        self.actionSaveState = QtGui.QAction(MainWindow)
        self.actionSaveState.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_state_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveState.setIcon(icon9)
        self.actionSaveState.setObjectName(_fromUtf8("actionSaveState"))
        self.slot0 = QtGui.QAction(MainWindow)
        self.slot0.setCheckable(True)
        self.slot0.setChecked(True)
        self.slot0.setObjectName(_fromUtf8("slot0"))
        self.slot1 = QtGui.QAction(MainWindow)
        self.slot1.setCheckable(True)
        self.slot1.setObjectName(_fromUtf8("slot1"))
        self.slot2 = QtGui.QAction(MainWindow)
        self.slot2.setCheckable(True)
        self.slot2.setObjectName(_fromUtf8("slot2"))
        self.slot3 = QtGui.QAction(MainWindow)
        self.slot3.setCheckable(True)
        self.slot3.setObjectName(_fromUtf8("slot3"))
        self.slot4 = QtGui.QAction(MainWindow)
        self.slot4.setCheckable(True)
        self.slot4.setObjectName(_fromUtf8("slot4"))
        self.slot5 = QtGui.QAction(MainWindow)
        self.slot5.setCheckable(True)
        self.slot5.setObjectName(_fromUtf8("slot5"))
        self.slot6 = QtGui.QAction(MainWindow)
        self.slot6.setCheckable(True)
        self.slot6.setObjectName(_fromUtf8("slot6"))
        self.slot7 = QtGui.QAction(MainWindow)
        self.slot7.setCheckable(True)
        self.slot7.setObjectName(_fromUtf8("slot7"))
        self.slot8 = QtGui.QAction(MainWindow)
        self.slot8.setCheckable(True)
        self.slot8.setObjectName(_fromUtf8("slot8"))
        self.slot9 = QtGui.QAction(MainWindow)
        self.slot9.setCheckable(True)
        self.slot9.setObjectName(_fromUtf8("slot9"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon10)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSaveScreenshot = QtGui.QAction(MainWindow)
        self.actionSaveScreenshot.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_screenshot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveScreenshot.setIcon(icon11)
        self.actionSaveScreenshot.setObjectName(_fromUtf8("actionSaveScreenshot"))
        self.actionResume = QtGui.QAction(MainWindow)
        self.actionResume.setEnabled(False)
        self.actionResume.setObjectName(_fromUtf8("actionResume"))
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setCheckable(True)
        self.actionPause.setEnabled(False)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon12)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionShowROMInfo = QtGui.QAction(MainWindow)
        self.actionShowROMInfo.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_rom_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowROMInfo.setIcon(icon13)
        self.actionShowROMInfo.setObjectName(_fromUtf8("actionShowROMInfo"))
        self.action1X = QtGui.QAction(MainWindow)
        self.action1X.setCheckable(True)
        self.action1X.setChecked(False)
        self.action1X.setObjectName(_fromUtf8("action1X"))
        self.action2X = QtGui.QAction(MainWindow)
        self.action2X.setCheckable(True)
        self.action2X.setObjectName(_fromUtf8("action2X"))
        self.action960x720 = QtGui.QAction(MainWindow)
        self.action960x720.setCheckable(True)
        self.action960x720.setObjectName(_fromUtf8("action960x720"))
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setCheckable(False)
        self.actionFullscreen.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_fullscreen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullscreen.setIcon(icon14)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionStatusBar = QtGui.QAction(MainWindow)
        self.actionStatusBar.setCheckable(True)
        self.actionStatusBar.setChecked(True)
        self.actionStatusBar.setVisible(True)
        self.actionStatusBar.setObjectName(_fromUtf8("actionStatusBar"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon15)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionMute = QtGui.QAction(MainWindow)
        self.actionMute.setCheckable(True)
        self.actionMute.setEnabled(False)
        self.actionMute.setObjectName(_fromUtf8("actionMute"))
        self.actionSlowDown = QtGui.QAction(MainWindow)
        self.actionSlowDown.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_speed_down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSlowDown.setIcon(icon16)
        self.actionSlowDown.setObjectName(_fromUtf8("actionSlowDown"))
        self.actionSpeedUp = QtGui.QAction(MainWindow)
        self.actionSpeedUp.setEnabled(False)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_speed_up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeedUp.setIcon(icon17)
        self.actionSpeedUp.setObjectName(_fromUtf8("actionSpeedUp"))
        self.action3X = QtGui.QAction(MainWindow)
        self.action3X.setCheckable(True)
        self.action3X.setObjectName(_fromUtf8("action3X"))
        self.actionCheats = QtGui.QAction(MainWindow)
        self.actionCheats.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action_cheats.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheats.setIcon(icon18)
        self.actionCheats.setObjectName(_fromUtf8("actionCheats"))
        self.actionCustom = QtGui.QAction(MainWindow)
        self.actionCustom.setObjectName(_fromUtf8("actionCustom"))
        self.actionLoadFrom = QtGui.QAction(MainWindow)
        self.actionLoadFrom.setEnabled(False)
        self.actionLoadFrom.setIcon(icon8)
        self.actionLoadFrom.setObjectName(_fromUtf8("actionLoadFrom"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setEnabled(False)
        self.actionSaveAs.setIcon(icon9)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionLimitFPS = QtGui.QAction(MainWindow)
        self.actionLimitFPS.setCheckable(True)
        self.actionLimitFPS.setChecked(True)
        self.actionLimitFPS.setEnabled(False)
        self.actionLimitFPS.setObjectName(_fromUtf8("actionLimitFPS"))
        self.actionSoftReset = QtGui.QAction(MainWindow)
        self.actionSoftReset.setEnabled(False)
        self.actionSoftReset.setIcon(icon15)
        self.actionSoftReset.setObjectName(_fromUtf8("actionSoftReset"))
        self.menuLoad.addAction(self.actionManually)
        self.menuLoad.addAction(self.actionFromList)
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadState)
        self.menuFile.addAction(self.actionSaveState)
        self.menuFile.addAction(self.menuStateSlot.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadFrom)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveScreenshot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionShowROMInfo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPaths)
        self.menuSettings.addAction(self.actionEmulator)
        self.menuSettings.addAction(self.actionPlugins)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menuEmulation.addAction(self.actionPause)
        self.menuEmulation.addAction(self.actionMute)
        self.menuEmulation.addSeparator()
        self.menuEmulation.addAction(self.actionStop)
        self.menuEmulation.addAction(self.actionReset)
        self.menuEmulation.addAction(self.actionSoftReset)
        self.menuEmulation.addSeparator()
        self.menuEmulation.addAction(self.actionLimitFPS)
        self.menuEmulation.addSeparator()
        self.menuEmulation.addAction(self.actionSlowDown)
        self.menuEmulation.addAction(self.actionSpeedUp)
        self.menuEmulation.addSeparator()
        self.menuEmulation.addAction(self.actionCheats)
        self.menuWindowSize.addAction(self.action1X)
        self.menuWindowSize.addAction(self.action2X)
        self.menuWindowSize.addAction(self.action3X)
        self.menuView.addAction(self.menuWindowSize.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFullscreen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEmulation.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "M64Py", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuLoad.setTitle(_translate("MainWindow", "&Open ROM", None))
        self.menuRecent.setTitle(_translate("MainWindow", "Open &Recent", None))
        self.menuStateSlot.setTitle(_translate("MainWindow", "Change State Slot", None))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menuEmulation.setTitle(_translate("MainWindow", "&Emulation", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menuWindowSize.setTitle(_translate("MainWindow", "Window Size", None))
        self.actionManually.setText(_translate("MainWindow", "&Manually...", None))
        self.actionFromList.setText(_translate("MainWindow", "From &List...", None))
        self.actionKeyboard.setText(_translate("MainWindow", "&Keyboard", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionClearHistory.setText(_translate("MainWindow", "&Clear history", None))
        self.actionPaths.setText(_translate("MainWindow", "Paths", None))
        self.actionGraphic.setText(_translate("MainWindow", "Graphics", None))
        self.actionEmulator.setText(_translate("MainWindow", "Emulator", None))
        self.actionPlugins.setText(_translate("MainWindow", "Plugins", None))
        self.actionLicense.setText(_translate("MainWindow", "&License", None))
        self.actionLoadState.setText(_translate("MainWindow", "Load State", None))
        self.actionLoadState.setShortcut(_translate("MainWindow", "F7", None))
        self.actionSaveState.setText(_translate("MainWindow", "Save State", None))
        self.actionSaveState.setShortcut(_translate("MainWindow", "F5", None))
        self.slot0.setText(_translate("MainWindow", "0", None))
        self.slot1.setText(_translate("MainWindow", "1", None))
        self.slot2.setText(_translate("MainWindow", "2", None))
        self.slot3.setText(_translate("MainWindow", "3", None))
        self.slot4.setText(_translate("MainWindow", "4", None))
        self.slot5.setText(_translate("MainWindow", "5", None))
        self.slot6.setText(_translate("MainWindow", "6", None))
        self.slot7.setText(_translate("MainWindow", "7", None))
        self.slot8.setText(_translate("MainWindow", "8", None))
        self.slot9.setText(_translate("MainWindow", "9", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionSaveScreenshot.setText(_translate("MainWindow", "&Save Screenshot", None))
        self.actionSaveScreenshot.setShortcut(_translate("MainWindow", "F12", None))
        self.actionResume.setText(_translate("MainWindow", "&Resume", None))
        self.actionPause.setText(_translate("MainWindow", "&Pause", None))
        self.actionPause.setShortcut(_translate("MainWindow", "P", None))
        self.actionStop.setText(_translate("MainWindow", "&Stop", None))
        self.actionStop.setShortcut(_translate("MainWindow", "Esc", None))
        self.actionShowROMInfo.setText(_translate("MainWindow", "Show ROM Info...", None))
        self.action960x720.setText(_translate("MainWindow", "960x720", None))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen", None))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "Alt+Return", None))
        self.actionStatusBar.setText(_translate("MainWindow", "Status Bar", None))
        self.actionReset.setText(_translate("MainWindow", "&Reset", None))
        self.actionReset.setShortcut(_translate("MainWindow", "F9", None))
        self.actionMute.setText(_translate("MainWindow", "&Mute", None))
        self.actionMute.setShortcut(_translate("MainWindow", "M", None))
        self.actionSlowDown.setText(_translate("MainWindow", "Slow Down", None))
        self.actionSlowDown.setShortcut(_translate("MainWindow", "F10", None))
        self.actionSpeedUp.setText(_translate("MainWindow", "Speed Up", None))
        self.actionSpeedUp.setShortcut(_translate("MainWindow", "F11", None))
        self.actionCheats.setText(_translate("MainWindow", "Cheats...", None))
        self.actionCheats.setShortcut(_translate("MainWindow", "F2", None))
        self.actionLoadFrom.setText(_translate("MainWindow", "Load State...", None))
        self.actionSaveAs.setText(_translate("MainWindow", "Save State As...", None))
        self.actionLimitFPS.setText(_translate("MainWindow", "Limit FPS", None))
        self.actionSoftReset.setText(_translate("MainWindow", "Sof&t Reset", None))
        self.actionSoftReset.setShortcut(_translate("MainWindow", "F8", None))

import images_rc
import icons_rc
