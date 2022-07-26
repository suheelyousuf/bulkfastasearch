#############################################################################
#  Tcl version 8.6
#  Jun 16, 2022 10:59:43 AM IST  platform: Ubuntu
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI Semilight} -size 14 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family {Segoe UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
vTcl:font:add_font \
    "-family {Segoe UI} -size 11 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font13
vTcl:font:add_font \
    "-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font14
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m55" -background {#33FFBD} 
    wm focusmodel $top passive
    wm geometry $top 600x450+295+130
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Bulk Fasta Search by Suheel Yousuf Wani"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab44 \
        -background {#33FFBD} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text {Bulk Fasta Search} 
    vTcl:DefineAlias "$top.lab44" "Label1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#33FFBD} -borderwidth 6 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Browse Fastsa File.....} 
    vTcl:DefineAlias "$top.but46" "fastaFileBt" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -background {#33FFBD} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} 
    vTcl:DefineAlias "$top.lab47" "fastaFilePathLab" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa48 \
        -background {#33FFBD} -foreground {#000000} \
        -font $::vTcl(fonts,vTcl:font12,object) -relief flat \
        -text {Enter the ID's seperated by commas(,)} 
    vTcl:DefineAlias "$top.tLa48" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex49 \
        -background white -font TkTextFont -foreground black -height 154 \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -width 334 -wrap word 
    .top42.tex49 configure -font "TkTextFont"
    .top42.tex49 insert end text
    vTcl:DefineAlias "$top.tex49" "idText" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -background {#33FFBD} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font13,object) -foreground {#000000} \
        -justify right -text Or 
    vTcl:DefineAlias "$top.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#33FFBD} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Browse ID's File....} 
    vTcl:DefineAlias "$top.but52" "idFileBt" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -background {#33FFBD} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} 
    vTcl:DefineAlias "$top.lab53" "idFilePathLab" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#33FFBD} -borderwidth 8 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -highlightthickness 2 -pady 0 -text Search 
    vTcl:DefineAlias "$top.but54" "searchBt" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m55
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab44 \
        -in $top -x 140 -y 0 -width 284 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 210 -y 70 -width 147 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 370 -y 80 -width 174 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa48 \
        -in $top -x 10 -y 180 -width 226 -relwidth 0 -height 39 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tex49 \
        -in $top -x 250 -y 130 -width 334 -relwidth 0 -height 154 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 170 -y 300 -width 64 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 250 -y 300 -width 127 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 390 -y 300 -width 184 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 230 -y 370 -width 157 -relwidth 0 -height 54 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

